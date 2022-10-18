from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

def document_initialised(driver):
    return driver.execute_script("return initialised")

# driver.get("file:///System/Volumes/Data/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/waits/index.html")
# WebDriverWait(driver, timeout=10).until(document_initialised)
# el = driver.find_element(By.TAG_NAME, "p")
# assert el.text == "Hello from JavaScript!"

# Мы передаем условие как ссылку на функцию, что ожидание будет выполняться неоднократно, пока его возвращаемое значение не будет истинным.
# «Правдивое» возвращаемое значение — это все, что оценивается как логическое значение «истина» в используемом языке, например строка,
#  число, логическое значение, объект (включая WebElement ) или заполненная (непустая) последовательность или список.
#  Это означает, что пустой список оценивается как false. Когда условие истинно и ожидание блокировки прерывается,
#  возвращаемое значение из условия становится возвращаемым значением ожидания.
#
# Зная это, а также поскольку утилита ожидания по умолчанию не игнорирует такие ошибки элементов ,
# мы можем реорганизовать наши инструкции, чтобы сделать их более краткими:

driver.get("file:///System/Volumes/Data/Users/anatolijfrolov/Documents/Projects/selenium/seleniumGettingStarted/waits/index.html")
el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"p"))
assert el.text == "Hello from JavaScript!"

# В этом примере мы передаем анонимную функцию (но мы также можем определить ее явно, 
# как делали ранее, чтобы ее можно было использовать повторно). 
# Первый и единственный аргумент, который передается нашему условию, всегда является ссылкой на наш объект драйвера, WebDriver . 
# В многопоточной среде вы должны быть осторожны при работе со ссылкой на драйвер, переданной в условие, а не со ссылкой на драйвер во внешней области.

# Поскольку ожидание не проглотит такие ошибки элемента, 
# которые возникают, когда элемент не найден, условие будет повторяться до тех пор, 
# пока элемент не будет найден. Затем он примет возвращаемое значение WebElement и передаст его обратно в наш скрипт.

# Если условие не выполняется, например, истинное возвращаемое значение из условия никогда не достигается, 
# ожидание вызовет/поднимет ошибку/исключение, называемое ошибкой тайм -аута .

