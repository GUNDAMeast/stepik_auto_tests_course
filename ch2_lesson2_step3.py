from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID,"num1").text) 
    y = int(browser.find_element(By.ID,"num2").text)

    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(x + y))

    browser.find_element(By.CSS_SELECTOR,"button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()