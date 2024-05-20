import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestHover:

    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        yield self.driver

        #self.driver.quit()
        print("Testing finished")

    def test_launch(self, setup):  # Ensure 'setup' fixture is passed
        self.driver.get("https://www.flipkart.com/")

    def test_hover(self, setup):  # Pass the fixture to the test method
        driver = setup
        wait = WebDriverWait(setup, 10)
        self.fashion = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Fashion']")))
        self.kids = driver.find_element((By.XPATH, "//a[text()='Kids']")))
        self.kid_sport = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Kids Sports Shoes']"))).click()

        ac = ActionChains(setup)
        ac.move_to_element(self.fashion).move_to_element(self.kids).move_to_element(self.kid_sport).click().perform()



