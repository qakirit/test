import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
t