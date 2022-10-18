from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


# def test():
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

def document_initialised(driver):
    return driver.execute_script("return initialised")

# driver.navigate("file:///System/Volumes/Data/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/waits/index.html")
driver.get("file:///System/Volumes/Data/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/waits/index.html")
WebDriverWait(driver, timeout=10).until(document_initialised)
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"

document_initialised(driver)
driver.quit()
