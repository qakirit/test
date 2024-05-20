import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)

#driver.get("http://www.deadlinkcity.com/")
driver.get("https://artoonsolutions.com/portfolio")
driver.maximize_window()
links = driver.find_elements(By.TAG_NAME, 'a')
count = 0



for link in links:
    url = link.get_attribute('href')  # Corrected 'href' attribute name
    try:
        response = requests.head(url) # response is obeject of request
        if response.status_code >= 400:
            print("Broken link:", url)
            count += 1
        else:
            print("Valid link:", url)
    except requests.RequestException as e:
        print(f"Error accessing link {url}: {e}")

print("Total broken links:", count)

driver.quit()
