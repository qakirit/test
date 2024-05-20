import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner

class Login_test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")


    def tearDown(self) -> None:
        self.driver.quit()

    def test_title_case(self):
        webpage_title = self.driver.title
        self.assertEqual("Test Login | Practice Test Automation", webpage_title, "Title page is not same")

    def test_negetive_login(self):
        print("Login with invalid credentials ")
        self.driver.find_element(By.ID, "username").send_keys("astudent")
        self.driver.find_element(By.ID, "password").send_keys("aPassword123")
        self.driver.find_element(By.ID, "submit")
        error='Your username is invalid!'
        self.assertEqual(error,"Your username is invalid!","Your test case is failed")


    def test_positive_login(self):
        print("Login with Valid credentials")
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Password123")
        self.driver.find_element(By.ID,"submit")

    def negetive_password(self):
        print("login with invalid password")
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Passwordd123")
        self.driver.find_element(By.ID, "submit")
        error = 'Your username is invalid!'
        self.assertEqual(error, "Your username is invalid!", "Your test case is failed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\kirit.solanki\\PycharmProjects\\test\\Results'))
