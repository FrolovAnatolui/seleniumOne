from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import TimeoutException

s = Service('geckodriver')
driver = webdriver.Firefox(service = s)
driver.get("file:///System/Volumes/Data/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/waits/index.html")

try:
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    element = wait.until(EC.element_to_be_clickable((By.ID, 'btn')))
    print('Успешно протестировано')
    driver.quit()
except TimeoutException:
    print("Ошибка времени ожидания")
    driver.quit()

