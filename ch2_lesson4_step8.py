from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    # вычисляет требуемое выражение и сразу отдаёт строкой
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID,"input_value").text
    answer = calc(x)

    browser.find_element(By.ID,"answer").send_keys(answer)

    browser.find_element(By.ID, "solve").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

    