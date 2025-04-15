import time
from playwright.sync_api import Playwright


def test_add_products_to_car_and_complete_the_order(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    # 2 seconds for website to load correctly - avoiding 500's errors
    time.sleep(2)
    page.goto("https://www.saucedemo.com/")

    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("visual_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")

    page.locator("[data-test=\"login-button\"]").click()

    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()

    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").type("David")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").type("Craig")
    page.locator("[data-test=\"lastName\"]").press("Tab")
    page.locator("[data-test=\"postalCode\"]").type("31815")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"cart-list\"] div").filter(has_text="1Sauce Labs OnesieRib snap").locator("[data-test=\"item-quantity\"]").click()

    page.locator("[data-test=\"finish\"]").click()
    finish_page_header = page.locator("[data-test=\"complete-header\"]")
    finish_page_header.click()
    page.locator("[data-test=\"back-to-products\"]").click()

    assert finish_page_header

    context.close()
    browser.close()