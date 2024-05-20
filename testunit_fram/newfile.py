from selenium import webdriver
from selenium.webdriver.common.by import  By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
