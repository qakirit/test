import requests
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver=webdriver.Firefox()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.get("https://artoonsolutions.com/portfolio")
driver.maximize_window()
link=driver.find_elements(By.TAG_NAME,'a')
count=0

for link_list in link:
    url_list=link_list.get_attribute('href')

    try:
        respones=requests.head(url_list)
        if respones.status_code>=400:
            print("Valid link:", url_list)
            count+=1
        else:
            print("Valid link:", url_list)

    except requests.RequestException as e:
        print(f"Error accessing link {url_list}: {e}")

print("Total broken links:", count)


