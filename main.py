from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.python.org/")


events= {}
find_dates = driver.find_elements(By.CSS_SELECTOR, 'div[class="medium-widget event-widget last"] ul[class="menu"] time ')
find_title = driver.find_elements(By.CSS_SELECTOR, 'div[class="medium-widget event-widget last"] ul[class="menu"] a')


for n in range(len(find_dates)):
    events[n] = {
        "time": find_dates[n].get_attribute("textContent"),
        "name": find_title[n].get_attribute("textContent")
    }


print(events)
