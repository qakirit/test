from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.edge
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,"//button[@aria-label='Previous Month']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Next Month']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Previous Month']").click()
driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']").click()
driver.find_element(By.XPATH,"//option[@value='11']").click()
driver.find_element(By.XPATH,"//div[@aria-label='Choose Monday, December 2nd, 2024']").click()