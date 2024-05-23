import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://www.saucedemo.com/")

time.sleep(2)
wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='submit-button btn_action']"))).click()

logo_text = driver.find_element(By.XPATH, "//div[@class='app_logo']")
actual_text = logo_text.text
expected_text = "Swag Labs"

assert actual_text == expected_text
print("Pass")
add_cart_button = driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")

for i in range(len(add_cart_button)):
    if i < 1:
        add_cart_button[i].click()
        break

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))).click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button ']"))).click()

driver.find_element(By.ID, "first-name").send_keys("Test")
driver.find_element(By.ID, "last-name").send_keys("First name")
driver.find_element(By.ID, "postal-code").send_keys("123456")
driver.find_element(By.ID, "continue").click()

summery_innfo = driver.find_element(By.XPATH, "//div[@class='summary_info']")

info = summery_innfo.text

print("Product ditails is " + info)
driver.find_element(By.ID, "finish").click()

order_text = driver.find_element(By.XPATH, "//h2[@class='complete-header']").text

ex_order_text = "Thank you for your order!"
driver.get_screenshot_as_file("screenshot1.png")
assert order_text == ex_order_text

driver.find_element(By.ID, "back-to-products").click()
add_cart_button = driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")

for i in range(len(add_cart_button)):
    time.sleep(3)

    if i <= 2:
        print("test is on goin", + i)
        # time.sleep(2)
        add_cart_button[i].click()
        time.sleep(3)
    else:
        pass

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))).click()

remove_buttons = driver.find_elements(By.ID, "remove-sauce-labs-backpack")

for i in range(len(remove_buttons)):
    if i <= 1:
        remove_buttons[i].click()


wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='continue-shopping']"))).click()