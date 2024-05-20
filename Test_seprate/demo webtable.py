from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://demoqa.com/broken")
image_element=driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa_1.jpg']")
is_broken = driver.execute_script("return arguments[0].naturalWidth === 0;", image_element)
#driver.execute_script("return argument[0].naturealWidh ==0; ",image_element)

if is_broken:
    print("The image is broken.")
else:
    print("The image is loaded successfully.")


