import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()

    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    # button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))).button.click()

    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = driver.find_element(By.ID, "book")
    button.click()

    t = driver.find_element(By.ID, 'input_value')
    x = t.text
    print(x)
    y = calc(x)
    input = driver.find_element(By.XPATH, '//*[@class="form-control"]')
    input.send_keys(y)
    driver.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)