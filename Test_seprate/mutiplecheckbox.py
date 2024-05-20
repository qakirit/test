from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Firefox()

driver.get("https://demo.automationtesting.in/Register.html")


checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkbox))

#approch 1

for i in range(len(checkbox)):
    checkbox[i].click()

#aaproch 2
'''for i in checkbox:

    i.click()
'''
driver.quit()