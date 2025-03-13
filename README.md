# LinkedIn Company Scraper

This is a Flask-based web service that scrapes LinkedIn company details using Selenium and stores the extracted data in an SQLite database.

## Features
- Scrapes company details from LinkedIn using `linkedin_scraper`.
- Uses Selenium for automated web scraping.
- Stores extracted data in an SQLite database.
- Provides an API endpoint to trigger scraping via a POST request.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- Selenium
- linkedin_scraper
- SQLite

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd linkedin-company-scraper
   ```

2. Install required dependencies:
   ```sh
   pip install flask selenium linkedin_scraper
   ```

3. Set up environment variables for LinkedIn credentials:
   ```sh
   export LINKEDIN_EMAIL="your_email@example.com"
   export LINKEDIN_PASSWORD="your_password"
   ```
   Or create a `.env` file and add:
   ```sh
   LINKEDIN_EMAIL=your_email@example.com
   LINKEDIN_PASSWORD=your_password
   ```

## Database Setup
The script will automatically create an SQLite database (`linkedin_data.db`) with a `company` table.

## Usage
### Running the Flask App
Start the Flask server:
```sh
python app.py
```

### API Endpoint
#### Scrape Company Details
- **Endpoint:** `POST /scrape`
- **Request Body:**
  ```json
  {
    "url": "https://www.linkedin.com/company/example"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Data stored successfully",
    "company_data": { ... }
  }
  ```

## Notes
- Ensure you have Chrome installed and the appropriate ChromeDriver version.
- LinkedIn may block scraping, so use it responsibly and consider using proxies if necessary.

## License
This project is licensed under the MIT License.

