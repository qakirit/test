import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_demo:
    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_01(self,setup):
        driver = setup
        print("test01")

    def test_02(self,setup):
        driver = setup
        print("test02")
