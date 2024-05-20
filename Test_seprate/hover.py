from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
firstname1=driver.find_element(By.XPATH,"//a[text()='Interactions ']")
firstname1.click()

move=driver.find_element(By.XPATH,"//a[text()='Drag and Drop ']")

end=driver.find_element(By.XPATH,"//a[text()='Static ']")

actions=ActionChains(driver)

actions.move_to_element(move).click().perform()

actions.move_to_element(end).click().perform()





