from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
#
# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
#
# print(count)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("John")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Rambo")
email = driver.find_element(By.NAME, "email")
email.send_keys("rambo@gmail.com")
email.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
