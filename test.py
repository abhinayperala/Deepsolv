from linkedin_scraper import Person, actions, Company
from selenium import webdriver
import os
driver = webdriver.Chrome()

email = os.getenv("LINKEDIN_EMAIL") 
password = os.getenv("LINKEDIN_PASSWORD")
actions.login(driver, email, password) 
company = Company("https://www.linkedin.com/company/google/", driver=driver)