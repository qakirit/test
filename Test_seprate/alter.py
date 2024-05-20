import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID,"alertButton").click()
time.sleep(3)
alert = Alert(driver)
alert.accept()




driver.find_element(By.ID,"timerAlertButton").click()
time.sleep(6)
alert.accept()

driver.find_element(By.ID,"confirmButton").click()
time.sleep(3)
alert.accept()

driver.find_element(By.ID,"promtButton").click()
time.sleep(3)
alert.send_keys("test")
alert.accept()