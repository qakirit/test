import unittest

# Assume you have a module named 'login' which contains the functions for login
from login import login_function

class TestLogin(unittest.TestCase):
    def test_successful_login(self):
        # Test successful login
        Username = "student"
        Password = "Password123"
        result = login_function(Username, Password) # funcation calling and store
        self.assertTrue(result)

    def test_failed_login(self):
        # Test failed login
        Username = "wrong_user"
        Password = "wrong_password"
        result = login_function(Username, Password)# funcation calling and store
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
