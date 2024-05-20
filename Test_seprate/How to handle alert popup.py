from selenium import webdriver
import urllib.parse

# URL that requires authentication
url = "https://digital.sundance.org/"

# Encode the password part of the URL
username = 'guest'
password = 'sundanceDev#20'
encoded_password = urllib.parse.quote(password)

# Create a WebDriver instance (you'll need the appropriate WebDriver for your browser)
driver = webdriver.Firefox()  # Example for Firefox - download the appropriate WebDriver for your browser

# Open the URL with credentials in the format: https://username:password@url
url_with_credentials = f'https://{username}:{encoded_password}@digital.sundance.org/'

# Open the URL
driver.get(url_with_credentials)

# Continue with your interactions with the authenticated page using Selenium
# For example:
# element = driver.find_element_by_id('some_id')
# element.click()  # Perform some action on the authenticated page


