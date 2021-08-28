from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import Config

driver = webdriver.Chrome(executable_path='/Users/shervinhaghgouy/Downloads/chromedriver')

# opening link in the browser
def open_web_page():
    url = Config.STARTINGURL
    driver.get(url)

# Navigate to the login page
def navigate_to_login():
    navToLogin = Config.HOMEUSERURL
    driver.get(navToLogin)

# input username/password and submit
def input_username_password():
    button = driver.find_element_by_id("username")
    button.send_keys(Config.USERNAME)
 
    button = driver.find_element_by_id("password")
    button.send_keys(Config.PASSWORD)
    button.send_keys(Keys.ENTER)

open_web_page()
navigate_to_login()
input_username_password()
