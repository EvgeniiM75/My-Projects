import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

bro = webdriver.Chrome()
bro.get("https://guru.qahacking.ru/")

try:
    bro.set_window_size(1366, 768)
    bro.find_element(By.XPATH, '//ul[@class="uk-navbar-nav"]/li[3]/a').click()
    bro.find_element(By.XPATH, '//ul[@class="uk-navbar-nav"]/li[3]/a').click()

    bro.find_element(
        By.XPATH, '//*[@class="product productitem_5"]/div/a').click()
    bro.find_element(By.ID, 'quantity').clear()
    bro.find_element(By.ID, 'quantity').send_keys(2)
    bro.find_element(By.XPATH, '//input[@type="submit"]').click()
    bro.find_element(By.XPATH, '//a[@class="btn btn-arrow-right"]').click()
    bro.find_element(By.XPATH, '//input[@name="f_name"]').send_keys("John")
    bro.find_element(By.XPATH, '//input[@name="l_name"]').send_keys("Machete")
    bro.find_element(
        By.XPATH, '//input[@name="email"]').send_keys("John@gmail.com")
    bro.find_element(By.ID, 'street').send_keys("Gagarin str")
    bro.find_element(By.ID, 'zip').send_keys("420000")
    bro.find_element(By.ID, 'city').send_keys("Kazan")
    bro.find_element(By.ID, 'state').send_keys("Tatarstan")

    select = Select(bro.find_element(By.ID, "country"))
    select.select_by_visible_text("Russian Federation")

    bro.find_element(By.ID, 'phone').send_keys("89370000000")
    bro.find_element(By.XPATH, '//input[@type="submit"]').click()

    bro.find_element(By.CSS_SELECTOR, '#payment_method_2').click()
    bro.find_element(By.CSS_SELECTOR, '#payment_submit').click()
    bro.find_element(By.CSS_SELECTOR, '#shipping_method_2').click()
    bro.find_element(By.XPATH, '//input[@type="submit"]').click()
    bro.find_element(By.XPATH, '//input[@type="checkbox"]').click()
    bro.find_element(By.XPATH, '//input[@name="finish_registration"]').click()

finally:
    # Даем время на просмотр и закрываем браузер
    time.sleep(10)
    bro.quit()
