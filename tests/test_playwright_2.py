import time, pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.parametrize("run", range(3))
def test_create_an_account(run, playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    # 2 seconds for website to load correctly - avoiding 500's errors
    time.sleep(2)
    page.goto("https://candymapper.com/")

    page.locator("#popup-widget307423-close-icon").click()
    page.locator("[id=\"\\34 \"]").click()
    page.get_by_role("link", name="Create Account").click()
    # time.sleep for ensuring that website will not reload by itself and lose filled textboxes
    time.sleep(3)
    page.get_by_role("textbox", name="First name").click()
    page.get_by_role("textbox", name="First name").type("John")
    page.get_by_role("textbox", name="Last name").click()
    page.get_by_role("textbox", name="Last name").type("Doe")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").type("john.doe@gmail.com")
    page.get_by_role("textbox", name="Phone (optional)").click()
    page.get_by_role("textbox", name="Phone (optional)").type("+48100200300")
    page.get_by_role("button", name="Create Account").click()
    time.sleep(3)

    check_your_email_notification = page.get_by_role("heading", name="Check your email")

    expect(check_your_email_notification).to_be_visible()
    #assert check_your_email_notification.is_visible()

    context.close()
    browser.close()
