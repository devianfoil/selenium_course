from selenium import webdriver
import math
import time
Link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()


browser.get(Link)
chest = browser.find_element_by_id("treasure")
x = chest.get_attribute("valuex")
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()
option2 = browser.find_element_by_id("robotsRule")
option2.click()
button = browser.find_element_by_css_selector("body > div > form > button")
button.click()

time.sleep(10)
browser.quit()