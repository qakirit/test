import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")

wait.until(EC.presence_of_element_located((By.ID, 'userName'))).send_keys("test")

list = ['os', 'abc@', '@dgmadil', 'test@gmail.com']
email_path = wait.until(EC.presence_of_element_located((By.ID, 'userEmail')))

# for i in list:
#     print(i)
email_path.clear()
email_path.send_keys(list[0])
wait.until(EC.element_to_be_clickable((By.ID, 'submit'))).click()


for i in list:

    email_path.clear()
    email_path.send_keys(i)
    wait.until(EC.element_to_be_clickable((By.ID, 'submit'))).click()
    time.sleep(2)


print("name",driver.find_element(By.ID,'name').text)
print("email",driver.find_element(By.ID,'email').text)
