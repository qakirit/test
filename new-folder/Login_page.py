from Pages.BasePage import BaseClass
from selenium.webdriver.common.by import By


class Login_Page_Class(BaseClass):  # Correct class name

    def __init__(self, driver):
        super().__init__(driver)
        self.user_input_element = (By.ID, "username")
        self.user_password_element = (By.ID, "password")
        self.submit_element = (By.ID, "submit")

    def enter_username(self, username):
        user_name_variable = self.explicitly_wait(self.user_input_element)
        if user_name_variable is not None:
            user_name_variable.send_keys(username)

    def enter_password(self, password):
        user_password_variable = self.explicitly_wait(self.user_password_element)
        if user_password_variable is not None:
            user_password_variable.send_keys(password)

    def click_on_the_submit_button(self):
        submit_button = self.explicitly_wait(self.submit_element)
        if submit_button is not None:
            submit_button.click()

    def login_check(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_the_submit_button()
