import unittest
import HtmlTestRunner
from selenium import webdriver

class Homepage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/logged-in-successfully/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_home_title(self):  # Renamed from 'hometitle' to 'test_home_title'
        expected_title = "Logged In Successfully"
        print(self.driver.title)
        assert self.driver.title == expected_title

    def test_one(self):  # Renamed from 'testone' to 'test_one'
        print("test")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\kirit.solanki\\PycharmProjects\\test\\Results'))
