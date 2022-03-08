from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()

    time.sleep(2)

    # переключения на новую вкладку (выбираем вторую вкладку)
    browser.switch_to.window(browser.window_handles[1])

    #забираю значение x
    """Атрибут text возвращает текст, который находится между открывающим и 
    закрывающим тегами элемента. Например, 
    text для данного элемента <div class="message">У вас новое сообщение
    .</div> вернёт строку: "У вас новое сообщение"."""


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла