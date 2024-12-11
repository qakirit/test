import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.blackbox.ai/agent/ImageGenerationLV45LJp")


wait = WebDriverWait(driver, 10)


upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Upload']")))
upload_button.click()


downloads_folder = r"C:\Users\kirit\Downloads"


image_files = [f for f in os.listdir(downloads_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]


if image_files:

    latest_image = max(image_files, key=lambda f: os.path.getmtime(os.path.join(downloads_folder, f)))
    latest_image_path = os.path.join(downloads_folder, latest_image)  # Full path to the latest image
    print(f"Uploading image: {latest_image_path}")
else:
    print("No image files found in the Downloads folder.")
    exit()


input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))


input_field.send_keys(latest_image_path)


time.sleep(5)
