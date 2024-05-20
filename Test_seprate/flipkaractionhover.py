import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")

wait = WebDriverWait(driver, 10)

time.sleep(2)
# Locate Fashion image
fashion = driver.find_element(By.XPATH, "//img[@alt='Fashion']")

act = ActionChains(driver)

act.move_to_element(fashion).perform()



kids = driver.find_element(By.XPATH, "//a[text()='Kids']")
act.move_to_element(kids).perform()

all = driver.find_element(By.XPATH, "//a[text()='All']")
act.move_to_element(all).click().perform()


act = ActionChains(driver)
act.move_to_element(fashion).perform()


