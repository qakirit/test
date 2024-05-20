import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class test_demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before Class Run")

    @classmethod
    def tearDownClass(cls):
        print("After Class Run")

    def setUp(self):
        print("Before Method Run")

    def tearDown(self):
        print("After method Run")

    def test01(self):
        print("01")

    def test02(self):
        print("02")

    def test03(self):
        print("03")

    @unittest.skip("This teest case under discussion")
    def test_skip(self):
        print("Skip test method")
    @unittest.skipIf(True,"we are not  testing todo result true")
    def test_skip_conditon(self):
        print("Skip test with conditon")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
