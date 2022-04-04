from selenium import webdriver
import time
Link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()


browser.get(Link)
x_element = browser.find_element_by_id("num1")
y_element = browser.find_element_by_id("num2")
x = x_element.text
y = y_element.text
z = int(x) + int(y)
u = str(z)
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select")).click()
select.select_by_value("u").click()
button = browser.find_element_by_css_selector("body > div > form > button")
button.click()
time.sleep(10)
browser.quit()
