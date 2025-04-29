from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x: str) -> str:
    # вычисляет требуемое выражение и сразу отдаёт строкой
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,"treasure").get_attribute("valuex")
    answer = calc(x)

    browser.find_element(By.ID,"answer").send_keys(answer)

    browser.find_element(By.ID, "robotCheckbox").click()

    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    