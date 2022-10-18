from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

s = Service('geckodriver')
driver = webdriver.Firefox(service = s)
driver.implicitly_wait(10)
driver.get("file:///System/Volumes/Data/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/waits/index.html")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
el = WebDriverWait(driver, timeout=2).until(lambda d: d.find_element(By.TAG_NAME,"p"))
# assert el.text == "hello"
driver.quit()
