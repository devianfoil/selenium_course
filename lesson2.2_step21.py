from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

Link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(Link)
    button1 = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button1.click()
    firs_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_name("text")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()