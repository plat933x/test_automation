from behave import given, when, then
from selenium.webdriver.common.by import By
import time

URL = "https://www.saucedemo.com/"
TEST_USER = "problem_user"
PASSWORD = "secret_sauce"

@given('SauceDemo URL loaded')
def given_step(context):
    context.driver = context.browser
    context.driver.get(URL)

@when('Username and password entered')
def when_step(context):
    context.driver.find_element(By.NAME, "user-name").send_keys(TEST_USER)
    context.driver.find_element(By.ID, "password").send_keys(PASSWORD)

@when('Login button clicked')
def when_step(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('Dashboard for logged users shall be visible')
def then_step(context):
    time.sleep(2)
    assert "Sauce Labs Backpack" in context.driver.page_source
    context.driver.quit()