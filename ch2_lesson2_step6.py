from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME,"firstname").send_keys("Ivan")
    browser.find_element(By.NAME,"lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID,         "country").send_keys("Russia")
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()