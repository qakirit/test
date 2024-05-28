import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BaseClass(unittest.TestCase):

    def __init__(self, driver):

        self.driver = driver

    def explicitly_wait(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"This element is not found: {locator}")
            return None
