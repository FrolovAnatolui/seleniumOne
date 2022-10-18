from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service

s = Service('geckodriver')
driver = webdriver.Firefox(service = s)
driver.get("file:///System/Volumes/Data/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/4elements/3finders/index.html")
fruits = driver.find_element(By.ID, "fruits")
fruit = fruits.find_element(By.CLASS_NAME,"tomatoes")
# vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
print(fruit)
