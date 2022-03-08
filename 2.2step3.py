from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_id("num1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    num1 = int(welcome_text)

    # находим элемент, содержащий текст
    welcome_text_elt2 = browser.find_element_by_id("num2")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text2 = welcome_text_elt2.text
    num2 = int(welcome_text2)

    print(num1)
    print(num2)

    # считаю
    z = int(num1) + int(num2)
    print(z)

    #выбираю
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value='{z}']").click()


    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
