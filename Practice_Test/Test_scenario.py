import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.launch_the_website()
        self.enter_user_name()
        self.enter_user_mobile()
        self.enter_password()
        self.click_on_loginbutton()
        self.check_alert_message()

    def launch_the_website(self):
        self.driver.get("https://www.amazon.in/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fs%3Fk%3Dlogin%2Bamazon%2Baccount%26adgrpid%3D59671903835%26ext_vrnc%3Dhi%26gclid%3DEAIaIQobChMI55XEydzPhAMViqpmAh3aOgBmEAAYASAAEgLIQ_D_BwE%26hvadid%3D590652406969%26hvdev%3Dc%26hvlocphy%3D9061748%26hvnetw%3Dg%26hvqmt%3De%26hvrand%3D11958339987125834033%26hvtargid%3Dkwd-837441119212%26hydadcr%3D24542_2265395%26tag%3Dgooginhydr1-21%26ref%3Dnav_ya_signin&prevRID=19CG9DQVVYVMSXT93R7B&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def enter_user_name(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, 'ap_customer_name'))).send_keys("")

    def enter_user_mobile(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, 'ap_phone_number'))).send_keys("12345680")

    def enter_password(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, 'ap_password'))).send_keys("Password")

    def click_on_loginbutton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, 'continue'))).click()

    def check_alert_message(self):
        wait = WebDriverWait(self.driver, 10)
        exp_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='auth-customerName-missing-alert']/div/div"))).text
        actual_text = "Enter your name"
        assert exp_text == actual_text

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\kirit.solanki\\PycharmProjects\\test\\testunit_fram\\out"))
