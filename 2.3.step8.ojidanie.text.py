from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #процеряев 12 секунд пока цена не будет равна 100
    number = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    print (number)

    #assert "true" in message.text

    #button = browser.find_element_by_class_name("btn.btn-primary")
    #пичарм советует новый вид написания:
    button = browser.find_element(by=By.CLASS_NAME, value="btn.btn-primary")
    button.click()

    time.sleep(2)

    # x_element = browser.find_element_by_id("input_value")
    #пичарм советует новый вид написания:
    x_element = browser.find_element(by=By.ID, value="input_value")
    x = x_element.text
    y = calc(x)

    #input1 = browser.find_element_by_id("answer")
    # пичарм советует новый вид написания:
    input1 = browser.find_element(by=By.ID, value="answer")
    input1.send_keys(y)


    # button = browser.find_element_by_id("solve")
    # пичарм советует новый вид написания:
    button = browser.find_element(by=By.ID, value="solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла