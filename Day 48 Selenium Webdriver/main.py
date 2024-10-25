from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url="https://www.prothom-alo.com")

input("Press enter to close the browser...")
driver.quit()
