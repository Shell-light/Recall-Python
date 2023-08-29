# import getpass
# my_password = getpass.getpass("What is your password?\n")
# print(my_password)
import time
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "http://www.instagram.com"
browser.get(url)

time.sleep(2)
username_el = browser.find_element(By.NAME, 'username')
username_el.send_keys(INSTA_USERNAME)

password_el = browser.find_element(By.NAME, 'password')
password_el.send_keys(INSTA_PASSWORD)

time.sleep(1.5)
submit_btn_el = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_btn_el.click()

body_el = browser.find_element(By.CSS_SELECTOR, "body")
html_text = body_el.get_attribute("innerHTML")

print(html_text)