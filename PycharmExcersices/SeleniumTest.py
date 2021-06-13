import selenium
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get("https://en-gb.facebook.com/login/")
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("YOUR_USER_NAME")

pas = driver.find_element_by_name("pass")
pas.clear()
pas.send_keys("YOUR_PASSWORD")
pas.send_keys(Keys.RETURN)

selenium.find_element_by_name("submit").click()

sleep(100)
driver.close()
