from flask import Flask, request, jsonify
import sqlite3
from linkedin_scraper import Company, actions
from selenium import webdriver
import os

app = Flask(__name__)

# LinkedIn credentials from environment variables
EMAIL = os.getenv("LINKEDIN_EMAIL")  # Set these in your system env
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Function to initialize SQLite DB
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

# Function to scrape company details
def scrape_company_details(company_url):
    # Setup Selenium WebDriver
    driver = webdriver.Chrome()

    # Log in to LinkedIn
    actions.login(driver, EMAIL, PASSWORD)

    # Scrape company details
    company = Company(company_url, driver=driver)
    driver.quit()  # Close browser after scraping

    # Extract relevant data
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

# Function to store data in SQLite
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
    
    # Validate request data
    if "url" not in data:
        return jsonify({"error": "Missing 'url' field in request"}), 400

    company_url = data["url"]
    
    try:
        # Scrape company details
        company_data = scrape_company_details(company_url)

        # Store in SQLite
        store_in_db(company_data)

        return jsonify({"message": "Data stored successfully", "company_data": company_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()  # Initialize database
    app.run(debug=True)
