import unittest
import HtmlTestRunner

class test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Before testing class")

    @classmethod
    def tearDownClass(cls):
        print("After testing class")

    def setUp(self):
        print("Before every method")

    def tearDown(self):
        print("After every method")

    @unittest.skipIf(True, "Test")
    def test_01(self):
        print("test01")

    def test_03(self):
        print("test03")

    @unittest.skip("test")
    def test_02(self):
        print("test02")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=""))