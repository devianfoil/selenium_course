from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try :
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    browser.execute_script("window.scrollBy(0, 300);")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    btn = browser.find_element_by_id("solve")
    btn.click()

finally:
    time.sleep(5)



