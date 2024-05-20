import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class testdemo(unittest.TestCase):

    def setUp(self) -> None:
        print("Before method")

    def tearDown(self) -> None:
        print("After Method")
    @unittest.skip("No need to test")
    def test_skip(self):
        print("Skip")
    @unittest.SkipTest
    def test_skip_with_test(self):
        print("test skip with tets")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
