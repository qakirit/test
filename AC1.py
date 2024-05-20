import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Firefox()

driver.maximize_window()
driver.get("https://demoqa.com/alerts")

driver.implicitly_wait(10)

wait = WebDriverWait(driver,10)

driver.find_element(By.ID,"alertButton").click()

alert = Alert(driver)
alert.accept()

driver.find_element(By.ID,"timerAlertButton").click()

time.sleep(6)
alert.accept()

driver.find_element(By.ID,"confirmButton").click()
alert.accept()

driver.find_element(By.ID,"promtButton").click()
alert.send_keys("test")
alert.accept()
