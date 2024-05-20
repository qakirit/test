import requests
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver=webdriver.Firefox()


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Print response data
print(response.json())




