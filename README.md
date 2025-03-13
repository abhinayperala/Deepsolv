# Deepsolv
```LinkedIn Company Scraper

This is a Flask-based web service that scrapes LinkedIn company details using Selenium and stores the extracted data in an SQLite database.

Features

Scrapes company details from LinkedIn using linkedin_scraper.

Uses Selenium for automated web scraping.

Stores extracted data in an SQLite database.

Provides an API endpoint to trigger scraping via a POST request.

Prerequisites

Ensure you have the following installed:

Python 3.x

Flask

Selenium

linkedin_scraper

SQLite

Installation

Clone the repository:

git clone <repository_url>
cd linkedin-company-scraper

Install required dependencies:

pip install flask selenium linkedin_scraper

Set up environment variables for LinkedIn credentials:

export LINKEDIN_EMAIL="your_email@example.com"
export LINKEDIN_PASSWORD="your_password"

Or create a .env file and add:

LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password

Database Setup

The script will automatically create an SQLite database (linkedin_data.db) with a company table.

Usage

Running the Flask App

Start the Flask server:

python app.py

API Endpoint

Scrape Company Details

Endpoint: POST /scrape

Request Body:

{
  "url": "https://www.linkedin.com/company/example"
}

Response:

{
  "message": "Data stored successfully",
  "company_data": { ... }
}

Notes

Ensure you have Chrome installed and the appropriate ChromeDriver version.
```
LinkedIn may block scraping, so use it responsibly and consider using proxies if necessary.

License

This project is licensed under the MIT License.
'''
