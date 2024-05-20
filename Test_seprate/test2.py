from  selenium import webdriver

from selenium.webdriver.chrome.service import service

servic_ojb=service("location")
driver=webdriver.chrome(service=service)

driver.get("URl")


#practies