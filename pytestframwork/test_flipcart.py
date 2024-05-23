import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class TestFlipkart:

    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_lunch(self, setup):
        driver = setup
        driver.get("https://www.flipkart.com/")
        wait = WebDriverWait(driver, 10)
        home = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Home & Furniture']")))
        act = ActionChains(driver)
        act.move_to_element(home).perform()
        tool = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tools & Utility']")))
        act.move_to_element(tool).perform()
        cloth = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Cloth Dryer Stand']")))
        act.move_to_element(cloth).click().perform()


    def test_search(self, setup):
        driver = setup
        driver.get("https://www.flipkart.com/")
        wait = WebDriverWait(driver, 10)
        search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='q']")))
        search.send_keys("mobile")
        time.sleep(3)
        #driver.findElement(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/ul/li[1]/div/a").click()
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/ul/li[1]/div/a").click()
