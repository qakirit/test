from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

driver=webdriver.Firefox()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://demoqa.com/checkbox")

wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='rct-checkbox']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@title='Expand all']"))).click()
checkboxes = driver.find_elements(By.XPATH, "//span[@class='rct-checkbox']")  # Find all checkbox elements
random_checkbox = random.choice(checkboxes)
random_checkbox.click()




