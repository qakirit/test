import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/sortable")


test = driver.find_element(By.XPATH,"//div[@id='demo-tabpane-list']/div[1]/div[6]")
sort = ActionChains(driver)
time.sleep(2)
sort.click_and_hold(test).move_by_offset(0,-50).perform()


