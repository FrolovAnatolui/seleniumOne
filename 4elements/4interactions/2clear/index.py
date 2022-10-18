from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

# Navigate to url
driver.get("http://www.google.com")
# Store 'SearchInput' element
SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("selenium")
driver.implicitly_wait(30)
# Clears the entered text
SearchInput.clear()
