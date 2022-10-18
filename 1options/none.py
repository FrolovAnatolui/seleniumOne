from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options = options)
driver.get("http://www.google.com")
driver.quit()
