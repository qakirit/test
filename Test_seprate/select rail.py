import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")

submit = driver.find_element(By.ID,"submit")
time.sleep(1)

driver.execute_script("arguments[0].scrollIntoView();",submit)




