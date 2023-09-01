# import getpass
# my_password = getpass.getpass("What is your password?\n")
# print(my_password)
import time
import requests
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

# print(html_text)

"""
<div class="_aacl _aaco _aacw _aad6 _aade" dir="auto">Follow</div>
"""
"""
<button class="_acan _acap _acas _aj1-" type="button"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x150jy0e x1e558r4 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh xl56j7k" style="height: 100%;"><div class="_aacl _aaco _aacw _aad6 _aade" dir="auto">Follow</div></div></button>
"""
# browser.find_elements(By.CSS_SELECTOR, "button")
# xpath
# my_button_xpath = "//button"
# browser.find_elements(By.XPATH, "my_button_xpath")
def click_to_follow(browser):
    # my_follow_btn_xpath = "//a[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    my_follow_btn_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    follow_btn_elments = browser.find_elements(By.XPATH, "my_follow_btn_xpath")
    for btn in follow_btn_elments:
        time.sleep(2) # self-throttle
        try:
            btn.click()
        except:
            pass

# new_user_url = "https://www.instagram.com/ted/"
# browser.get(new_user_url)


time.sleep(2)
the_rock_url = ""
browser.get(the_rock_url)