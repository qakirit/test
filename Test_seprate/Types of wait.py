from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

driver = webdriver.Firefox()

#wait = WebDriverWait(driver, 10) declaration

wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

firstname=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='First Name']")))
firstname.send_keys("test")



driver.quit()
