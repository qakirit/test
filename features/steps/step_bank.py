import time

from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@given(u': Launch the webbowser')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when(u': I am on the login page')
def step_impl(context):
    context.driver.get("https://practicetestautomation.com/practice-test-login/")


@then(u': entering the   "{user}" and "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.ID, 'username').send_keys(user)
    time.sleep(2)

    context.driver.find_element(By.ID, 'password').send_keys(pwd)

    time.sleep(3)
    context.driver.find_element(By.ID, 'submit').click()


@then(u': close the browser')
def step_impl(context):
    context.driver.quit()
