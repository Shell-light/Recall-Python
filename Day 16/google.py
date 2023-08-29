import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() # Firefox()

url = 'http://google.com'
browser.get(url)

"""
<input type='text' class='' id='' name='??' />
<textarea name='??'><textarea>
<textarea name="q"   type="search" ></textarea>
"""
time.sleep(2)
name = 'q'
search_el = browser.find_element(By.NAME, 'q')
# print(search_el)
# search_el = browser.find_element_css_selector("h1")
search_el.send_keys("selenium python")
"""
<input type='submit' />
<button type='submit' />
<form></form>

<input type="submit">
"""
submit_btn_el = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()

