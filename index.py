from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    # Синхронизация кода с текущим состоянием браузера — одна из самых больших проблем с Selenium, и сделать это хорошо — сложная тема.
    # По сути, вы хотите убедиться, что элемент находится на странице, прежде чем вы попытаетесь найти его, и что элемент находится в интерактивном состоянии, прежде чем вы попытаетесь взаимодействовать с ним.
    # Неявное ожидание редко бывает лучшим решением, но здесь его проще всего продемонстрировать, поэтому мы будем использовать его в качестве заполнителя.
    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()

test()
