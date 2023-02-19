# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.ID, "verify")))
# button.click()

button = WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), text_="100"))
button_book = browser.find_element(By.ID, value="book")
button_book.click()

x_element = browser.find_element(By.ID, value="input_value").text
value_x = calc(x_element)

field_insert_x = browser.find_element(By.ID, value="answer")
field_insert_x.send_keys(value_x)

button1 = browser.find_element(By.CSS_SELECTOR, value="button[type='submit']")
button1.click()

time.sleep(10)
browser.quit()
