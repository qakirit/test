import unittest
import HtmlTestRunner
from selenium import webdriver


class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before test Class")

    @classmethod
    def tearDownClass(cls):
        print("After Test class")

    def setUp(self):
        print("Before method")

    def tearDown(self):
        print("After Test mehod")

    @unittest.skip("No")
    def test_skip(self):
        print("Test case")

    @unittest.skipIf(True, "Yes")
    def tes_skip_con(self):
        print("Tets")

    def test01(self):
        print("01")

    def test02(self):
        print("02")

    def test03(self):
        print("03")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
