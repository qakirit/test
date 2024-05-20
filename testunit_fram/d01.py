import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class d_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test Before Class")
    @classmethod
    def tearDownClass(cls):
        print("Test after class")
    def setUp(self):
        print("test before every method")
    def tearDown(self):
        print("test atter every method")
    def test_01(self):
        print("test 01")
    def test_02(self):
        print("test 02")
    @unittest.skipIf(True,"test")
    def test_03(self):
        print("test 03")
    @unittest.skip
    def test_04(self):
        print("test 04")

if __name__ == "__main__" :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
