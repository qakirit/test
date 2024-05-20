import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class test_demo(unittest.TestCase):

    def setUp(self) -> None:
        print("Test before Every method")

    def tearDown(self) -> None:
        print("Test After Every method")

    def test_print(self):
        print("test")

    @unittest.skip
    def test_skip(self):
        print("skip test due ")
    @unittest.SkipTest
    def test_skip_with_reason(self):
        print("skip test with reason")

    @unittest.skipIf(1, "if a is equal no 1")
    def test_skip_with_condition(self):
        print("Skip test with Condition")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
