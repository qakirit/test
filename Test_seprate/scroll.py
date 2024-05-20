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
driver.get("https://demoqa.com/automation-practice-form")

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
element = driver.find_element(By.XPATH,"")
driver.execute_script("arguments[0].scrollIntoView()", element)
driver.execute_script("window.scrollBy(0, 500)")
