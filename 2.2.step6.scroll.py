from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    # говорим откулда брать
    x_element = browser.find_element_by_id ("input_value")
    # забираем текст
    x = x_element.text
    y = calc(x)

    time.sleep(2)

    # говорим скролль до элемента
    #button = browser.find_element_by_css_selector("button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100);")

    # считаю и вставляю ответ в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    time.sleep(2)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    time.sleep(2)

    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()
    time.sleep(2)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла