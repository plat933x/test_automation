from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from behave import fixture, use_fixture


@fixture
def selenium_browser_chrome(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    context.browser = webdriver.Chrome(service=service, options=options)
    yield context.browser
    context.browser.quit()

def before_all(context):
    use_fixture(selenium_browser_chrome, context)

def after_all(context):
    if hasattr(context, "browser"):
        context.browser.quit()
