from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload")
driver.save_screenshot('4elements/1fileUpload/selenium-snapshot.png')
driver.find_element(By.ID,"file-upload").send_keys('/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/4elements/1fileUpload/selenium-snapshot.png')
driver.find_element(By.ID,"file-submit").submit()
if(driver.page_source.find("File Uploaded!")):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()

