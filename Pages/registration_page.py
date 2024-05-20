# pages/registration_page.py

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id('username').send_keys(username)

    def enter_email(self, email):
        self.driver.find_element_by_id('email').send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id('password').send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_id('submit').click()

    def get_success_message(self):
        return self.driver.find_element_by_id('success-message').text
