from flask import Flask, request, jsonify
import sqlite3
from linkedin_scraper import Company, actions
from selenium import webdriver
import os

app = Flask(__name__)

EMAIL = os.getenv("LINKEDIN_EMAIL")  
PASSWORD = os.getenv("LINKEDIN_PASSWORD")


def init_db():
    conn = sqlite3.connect("linkedin_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT UNIQUE,
            linkedin_id TEXT,
            profile_picture TEXT,
            description TEXT,
            website TEXT,
            industry TEXT,
            followers INTEGER,
            head_count TEXT,
            specialities TEXT
        )
    """)
    conn.commit()
    conn.close()

def scrape_company_details(company_url):
   
    driver = webdriver.Chrome()

    
    actions.login(driver, EMAIL, PASSWORD)

   
    company = Company(company_url, driver=driver)
    driver.quit()  

    
    return {
        "name": company.name,
        "url": company_url,
        "id": company.linkedin_id,
        "profile_picture": company.profile_picture_url,
        "description": company.about_us,
        "website": company.website,
        "industry": company.industry,
        "followers": company.followers,
        "head_count": company.headcount,
        "specialities": ", ".join(company.specialities) if company.specialities else None,
    }


def store_in_db(company_data):
    conn = sqlite3.connect("linkedin_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO company 
        (name, url, linkedin_id, profile_picture, description, website, industry, followers, head_count, specialities)
        VALUES (:name, :url, :id, :profile_picture, :description, :website, :industry, :followers, :head_count, :specialities)
    """, company_data)

    conn.commit()
    conn.close()

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.get_json()
    
   
    if "url" not in data:
        return jsonify({"error": "Missing 'url' field in request"}), 400

    company_url = data["url"]
    
    try:
    
        company_data = scrape_company_details(company_url)

       
        store_in_db(company_data)

        return jsonify({"message": "Data stored successfully", "company_data": company_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db() 
    app.run(debug=True)
