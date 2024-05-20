from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Define the username and password
username = "guest"
password = "sundanceDev#20"

# Encode the username and password
encoded_username = quote(username, safe='')
encoded_password = quote(password, safe='')

# Construct the URL with embedded credentials
url = f"https://{encoded_username}:{encoded_password}@digital.sundance.org/sign-in"

# Create a Firefox WebDriver instance with a custom timeout
driver = webdriver.Firefox()
driver.maximize_window()
driver.set_page_load_timeout(60)  # Increase the timeout to 60 seconds

# Open the webpage with basic authentication
try:
    driver.get(url)
except TimeoutException:
    print("Page load timed out")

wait = WebDriverWait(driver, 30)

# Find and fill the email field
email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
email_field.send_keys("ki@yopmail.com")

# Find and fill the password field
password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
password_field.send_keys("Artoon1#")

# Click the submit button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sd_form_submit']/button")))
submit_button.click()
