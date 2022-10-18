from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# Условие ожидания можно настроить в соответствии с вашими потребностями. 
# Иногда нет необходимости ждать полного тайм-аута по умолчанию, так как штраф за невыполнение успешного условия может быть дорогостоящим.

# Ожидание позволяет вам передать аргумент, чтобы переопределить тайм-аут:

# WebDriverWait(driver, timeout=3).until(some_condition)
