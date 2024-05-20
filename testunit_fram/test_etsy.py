import time

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class Etsy(unittest.TestCase):
    driver = None
    wait = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        cls.driver.get("https://www.etsy.com/")


    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        print("test")

    def test_search(self):
        time.sleep(10)
        self.driver.find_element(By.ID, "global-enhancements-search-query").send_keys("test")
        time.sleep(2)
        self.driver.find_element(By.ID, "global-enhancements-search-query").send_keys(Keys.DOWN)
        self.driver.find_element(By.ID, "global-enhancements-search-query").send_keys(Keys.ENTER)
        time.sleep(4)
        self.driver.find_element(By.ID,"listing-title-1403799739").click()
        time.sleep(3)
        imte = self.driver.find_element(By.XPATH,"//p[text()='Only 1 left and in 1 cart']").text
        print("testing ijfoi "+imte)
        self.driver.find_element(By.XPATH,"//*[@id='listing-page-cart']/div[6]/div[1]/div[2]/div[2]/div/form/div").click()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
