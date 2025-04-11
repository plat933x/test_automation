from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from behave import fixture, use_fixture


@fixture
def browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    context.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.browser.implicitly_wait(8)
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(browser, context)

def after_all(context):
    if hasattr(context, "browser"):
        context.browser.quit()
