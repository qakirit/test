# login.py

def login_function(Username, Password):
    # Here you would implement the actual login functionality
    # For the sake of this example, let's assume a simple check
    # where the login succeeds if the username and password are both "admin"
    if Username  == "student" and Password  == "Password123":
        return True
    else:
        return False
