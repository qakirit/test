from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page():
    def __init__(self,driver):
        self.driver=driver
        self.user_name = (By.ID, "username")
        self.user_password = (By.ID, "password")
        self.loing_button = (By.ID, "submit")

