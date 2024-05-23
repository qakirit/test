from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



class Test:

    @pytest.fixture(scope="funcation")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_01(self,setup):
        driver = setup
