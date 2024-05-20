from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Explicit wait for the element with link text "Digital downloads"
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Digital downloads")))

element.click()  # Click the element after it's located

#driver.quit()
