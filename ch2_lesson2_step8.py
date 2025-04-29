from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

link = "https://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME,"firstname").send_keys("Ivan")
    browser.find_element(By.NAME,"lastname").send_keys("Petrov")
    browser.find_element(By.NAME,"email").send_keys("IvanPetrov@mail.com")
    browser.find_element(By.ID,"file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR,"button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла