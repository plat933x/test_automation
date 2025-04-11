from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):

    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    context.browser = webdriver.Chrome(options=options)
    context.browser.implicitly_wait(8)

def after_all(context):
    context.browser.quit()
