from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
browser.execute_script("window.scrollBy(0, 100);")
input = browser.find_element_by_id("answer")
input.send_keys(y)
option1 = browser.find_element_by_css_selector("body > div > form > div.form-check.form-check-custom > label")
option1.click()
option2 = browser.find_element_by_css_selector("body > div > form > div.form-check.form-radio-custom > label")
option2.click()
button = browser.find_element_by_css_selector("body > div > form > button")
button.click()
time.sleep(10)
browser.quit()

