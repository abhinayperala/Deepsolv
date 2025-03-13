from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "abhinay.perala@gmail.com"
password = "intermediate2021"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/joey-sham-aa2a50122", driver=driver)