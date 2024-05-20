import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearch:

    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        yield self.driver
       # self.driver.quit()

    def test_launch(self, setup):
        driver = setup
        driver.get("https://www.flipkart.com/")

    def test_click_on_search(self, setup):
        driver = setup
        wait = WebDriverWait(driver,10)
        search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        search_input.send_keys("Mobile")

    def test_display(self, setup):

        driver = setup
        wait = WebDriverWait(driver, 10)
        print("test are you okay ??")
        search_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='_3D0G9a']")))
        #for element in search_elements:
         #   product_name = element.text
          #  print("Product name is " + product_name)
    def test_display_click(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_2iLD__']"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='vivo T2x 5G (Sunstone Orange, 128 GB)']"))).click()




