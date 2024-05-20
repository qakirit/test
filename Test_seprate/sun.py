import requests

# Set your username and password
username = "guest"
password = "sundanceDev#20"

# URL of the site with authentication
url = 'https://digital.sundance.org/program/films/'

# Create a session object
session = requests.Session()

# Perform a POST request to authenticate
login_url = 'https://digital.sundance.org/login'  # Update with the actual login URL
login_data = {
    'username': username,
    'password': password
}
response = session.post(login_url, data=login_data)

# Check if login was successful
if response.status_code == 200:
    # Now perform a GET request to access the authenticated page
    response = session.get(url)

    # Check if access to the page was successful
    if response.status_code == 200:
        # Print the content of the page
        print(response.text)
    else:
        print("Failed to access the page:", response.status_code)
else:
    print("Login failed:", response.status_code)
