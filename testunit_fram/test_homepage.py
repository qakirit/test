import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner


class Homepage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://practicetestautomation.com/logged-in-successfully/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_home_title(self):  # Renamed from 'hometitle' to 'test_home_title'
        expected_title = "Logged In Successfully | Practice Test Automation"
        print(self.driver.title)
        assert self.driver.title == expected_title

    def test_one(self):  # Renamed from 'testone' to 'test_one'
        expect_text = "Congratulations student. You successfully logged in!"
        text_is = self.driver.find_element(By.XPATH,
                                           "//strong[text()='Congratulations student. You successfully logged in!']")
        assert text_is.text == expect_text

    def test_logout_button(self):

        try:
            log_out = self.driver.find_element(By.XPATH, "//a[text()='Log out']")
            assert log_out.is_displayed(), "The logout button is not display"
        except NoSuchElementException:
            self.assertFalse("Login button not found")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out'))
