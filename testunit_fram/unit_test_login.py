import unittest

import HtmlTestRunner
from  selenium import  webdriver
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC
from  selenium.webdriver.common.by import By


class test_home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("")

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=""))


