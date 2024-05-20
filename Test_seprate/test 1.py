from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#driver = webdriver.Chrome()
driver = webdriver.Edge()

driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

#driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("sachinn")
#element = driver.find_element_by_xpath("//input[@placeholder='First Name']")
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Firstname")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("lastname")
driver.find_element(By.XPATH, " //textarea[@rows='3']").send_keys("Mountain Standard Time (MST) is 7 hours behind Coordinated Universal Time (UTC). This time zone is in use during standard time in: North America.")
driver.find_element(By.XPATH, " //input[@type='email']").send_keys("email@gmail.com")
driver.find_element(By.XPATH, "  //input[@type='tel']").send_keys("email@gmail.com")



