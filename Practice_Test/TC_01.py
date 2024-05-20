import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Mone_logoin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
    def test_Mone_logoin(self):
        self.test_lunch_the_website()
        self.test_login()
        self.test_name()
        self.test_passwod()
        self.test_login()
        self.test_verify()

    def test_lunch_the_website(self):
        self.driver.get('http://moneymyntra.co.in/FinnSys/default.asp')

    def test_login_as(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//select[@name='LOGINAS']"))).click()
    def test_name(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located((By.NAME,'LoginName'))).send_keys("Testuser")
    def test_passwod(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located((By.NAME,'password'))).send_keys("Password")

    def test_login(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type ='submit']"))).click()
    def test_verify(self):
        wait = WebDriverWait(self.driver, 10)
        eror_message = wait.until(EC.presence_of_element_located((By.XPATH, "//b[text()='Error:']"))).text
        expe_message = "Error:"
        assert expe_message == eror_message


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))

