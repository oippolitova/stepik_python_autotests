from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
        
    # Ваш код
    # Дождаться, когда цена уменьшится до 100
    text1 = WebDriverWait(browser, 8).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1 = browser.find_element_by_id("book")
    button1.click()
    
    #button1 = browser.find_element_by_id("book")
    #button1.click()
    
            
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    # Отправляем заполненную форму
    button2 = browser.find_element_by_id("solve")
    button2.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()