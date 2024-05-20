import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_demo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Befor Class Run")

    @classmethod
    def tearDownClass(cls) -> None:
        print("After Class Run")

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/logged-in-successfully/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_home_title(self):  # Renamed from 'hometitle' to 'test_home_title'
        expected_title = "Logged In Successfully | Practice Test Automation"
        print(self.driver.title)
        assert self.driver.title == expected_title

if __name__ =="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
