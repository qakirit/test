from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
wait=WebDriverWait(driver,10)

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
first_name=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='First Name']")))
first_name.send_keys("tes")




#firstname=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='First Name']")))
#firstname.send_keys("test")