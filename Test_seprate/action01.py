import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(2)

interactions = driver.find_element(By.XPATH, "//a[text()='Interactions ']")
drag_drop = driver.find_element(By.XPATH, "//a[text()='Drag and Drop ']")
dynamic = driver.find_element(By.XPATH, "//a[text()='Dynamic ']")
static = driver.find_element(By.XPATH, "//a[text()='Static ']")

act = ActionChains(driver)
act.move_to_element(interactions).perform()
time.sleep(2)

act.move_to_element(drag_drop).perform()
time.sleep(2)

act.move_to_element(dynamic).perform()
time.sleep(2)

act.move_to_element(static).perform()

driver.quit()
