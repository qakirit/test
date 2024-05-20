import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import HtmlTestRunner


class testclass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def tearDown(self):
        self.driver.quit()

    def test01(self):
        self.title = "Test login"
        ex_title = self.driver.find_element(By.XPATH,"//h2[text()='Test login']").text
        self.assertEqual(self.title,ex_title,"Not matach")

    def test02(self):
        self.driver.find_element(By.ID, "username").send_keys("student")

        self.driver.find_element(By.ID, "password").send_keys("Password123")

        self.driver.find_element(By.ID, "submit").click()


if __name__ == "__ main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))