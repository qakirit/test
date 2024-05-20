import unittest

import HtmlTestRunner
from selenium import webdriver


class Test_demo(unittest.TestCase):

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

if __name__ == "__ main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))




