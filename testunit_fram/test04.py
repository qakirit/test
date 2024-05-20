import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before class")

    @classmethod
    def tearDownClass(cls):
        print("After Class")

    def setUp(self):
        print("Before every methodd")

    def tearDown(self):
        print("After Every method")

    def test01(self):
        print("test one ")

    def test02(self):
        print("test one ")
    @unittest.skipIf(True,"Test ok")
    def test03(self):
        print("test one ")

    @unittest.skip
    def test04(self):
        print("skip one ")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
