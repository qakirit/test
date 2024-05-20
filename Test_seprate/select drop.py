from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

# Find the dropdown element for states
state_dropdown = driver.find_element(By.XPATH, "//div[@id='stateCity-wrapper']//div[@id='state']//select")

# Extract options from the dropdown
state_options = state_dropdown.find_elements(By.TAG_NAME, "option")

# Extract state names from options
state_names = [option.text for option in state_options]

# Print the list of state names
print(state_names)
