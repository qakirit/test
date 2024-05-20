import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")
time.sleep(5)
ele = driver.find_element(By.XPATH,"//span[text()='Electronics']")
time.sleep(2)
act = ActionChains(driver)
act.move_to_element(ele).perform()

health = driver.find_element(By.XPATH,"//a[text()='Health & Personal Care']")# move element-> one slide to another slider
time.sleep(2)
act.move_to_element(health).perform() # move element-> one slide to another slider

test = driver.find_element(By.XPATH,"//a[text()='Epilators']")
time.sleep(2)
act.move_to_element(test).click().perform()

