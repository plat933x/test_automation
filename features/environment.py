from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):

    driver_path = "drivers/chromedriver"

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    context.browser = webdriver.Chrome(executable_path=driver_path, options=options)
    context.browser.implicitly_wait(8)

def after_all(context):
    context.browser.quit()
