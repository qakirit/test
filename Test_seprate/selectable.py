import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/droppable")

driver.find_element(By.ID, "droppableExample-tab-accept").click()
test = driver.find_element(By.ID, "acceptable")
tes1 = driver.find_element(By.ID, "notAcceptable")
move = driver.find_element(By.XPATH, "//div[@id='acceptDropContainer']/div[@id='droppable']")

sort = ActionChains(driver)
time.sleep(3)

sort.click_and_hold(test).move_to_element(move).perform()

time.sleep(3)
sort.click_and_hold(tes1).move_to_element(move).release().perform()
