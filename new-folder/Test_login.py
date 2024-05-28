import unittest
from selenium.webdriver.common.by import By
from Pages.Login_page import Login_Page_Class  # Correct class name
from selenium import webdriver


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def tearDown(self):
        self.driver.quit()

    def test_login_case(self):
        run = Login_Page_Class(self.driver)
        run.login_check("student", "Password123")  # Ensure the correct password


if __name__ == "__main__":
    unittest.main()
