import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, StaleElementReferenceException, TimeoutException
import HtmlTestRunner

class ExceptionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/practice-test-exceptions/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_noSuchElementException(self):
        try:
            self.driver.find_element(By.ID, "save_btn").click()
        except NoSuchElementException:
            self.fail("NoSuchElementException occurred")

    def test_elementNotInteractableException(self):
        try:
            element = self.driver.find_element(By.ID, "displayed-text")
            element.click()
        except ElementNotInteractableException:
            self.fail("ElementNotInteractableException occurred")

    def test_invalidElementStateException(self):
        try:
            element = self.driver.find_element(By.ID, "colorChange")
            element.send_keys("invalid_state")
        except InvalidElementStateException:
            self.fail("InvalidElementStateException occurred")

    def test_staleElementReferenceException(self):
        try:
            element = self.driver.find_element(By.ID, "remove-text")
            self.driver.refresh()  # Causes the element to become stale
            element.text
        except StaleElementReferenceException:
            self.fail("StaleElementReferenceException occurred")

    def test_timeoutException(self):
        try:
            self.driver.find_element(By.ID, "invisible-btn").click()
        except TimeoutException:
            self.fail("TimeoutException occurred")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Results'))
