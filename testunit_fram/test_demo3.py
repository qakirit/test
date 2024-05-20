import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_demo_three(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://practicetestautomation.com/logged-in-successfully/")
        print("Before Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("After Class")
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://practicetestautomation.com/logged-in-successfully/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_print(self):
        print("Test")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))