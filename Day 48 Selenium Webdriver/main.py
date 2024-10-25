from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(url="https://www.python.org/")

events_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")
events = [event.find_element(By.TAG_NAME, "a").text for event in events_elements]
time_list = [event.find_element(By.TAG_NAME, "time").get_attribute(name="datetime").split("T")[0] for
             event in events_elements]

events_data = {}
for i in range(len(events)):
    events_data[i] = {
        "time": time_list[i],
        "name": events[i]
    }

print(events_data)
driver.quit()
