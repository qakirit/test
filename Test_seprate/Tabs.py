import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get('https://demoqa.com/auto-complete')

type_mult = wait.until(EC.element_to_be_clickable((By.ID, 'autoCompleteMultipleContainer')))
type_mult.click()
type_mult_input = wait.until(EC.element_to_be_clickable((By.ID, 'autoCompleteMultipleInput')))
type_mult_input.send_keys("Yellow")

time.sleep(2)
# Send TAB key to move to the next element
type_mult_input.send_keys(Keys.TAB)
