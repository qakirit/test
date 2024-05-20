from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
wait = WebDriverWait(driver,10)
# Switch to the 'Accept' tab


driver.find_element(By.ID,"promtButton").click()
time.sleep(3)

driver.switch_to.alert.send_keys("tets test")

driver.switch_to.alert.accept()

