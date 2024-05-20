from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()  #

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

mul_check=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and contains(@id,'day')]")

print(len(mul_check))

'''for i in range(len(mul_check)):
    mul_check[i].click()'''

#select multple checkboxes by choice

for checkbox in mul_check:
    weekname=checkbox.get_attribute('id')
    if weekname=='monday' or weekname=='sunday' :
        checkbox.click()


driver.quit()

