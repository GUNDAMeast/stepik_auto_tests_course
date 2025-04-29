from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x: str) -> str:
    # вычисляет требуемое выражение и сразу отдаёт строкой
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID,"input_value").text
    answer = calc(x)

    browser.find_element(By.ID,"answer").send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    