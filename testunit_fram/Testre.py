import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner


class login_test_lear(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def tearDown(self):
        self.driver.quit()

    def test01_title(self):
        web_title = self.driver.title
        self.assertEqual("Test Login | Practice Test Automation", web_title, "Title page is not same")

    def test02_negetive(self):
        self.driver.find_element(By.ID, "username").send_keys("astudent")
        self.driver.find_element(By.ID, "password").send_keys("aPassword123")

    def test03_positive_login(self):  # corrected method name
        print("Login with Valide -")
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Password123")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\pytestframwork\\output"))
