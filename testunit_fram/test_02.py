import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before all tests in the class")

    @classmethod
    def tearDownClass(cls):
        print("After all tests in the class")

    def setUp(self):
        print("Before each test method")

    def tearDown(self):
        print("After each test method")

    def test01(self):
        print("Test 01 Run")

    def test02(self):
        print("test 02 Run")

    @unittest.skip("No need to test now")
    def test_skip(self):
        print("Skip with Reason")

    @unittest.skipIf(True, "Result doesn't match")
    def test_skip_with_condition(self):
        print("Skip with condition")

    def test03(self):
        print("Test run 03")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
