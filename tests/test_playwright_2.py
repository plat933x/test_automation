import time, pytest
from playwright.sync_api import Playwright

@pytest.mark.parametrize("run", range(10))
def test_create_an_account(run, playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://candymapper.com/")
    page.locator("#popup-widget25042-cta").click()
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

    check_your_email_notification = page.locator("//h4[contains(.,'Check your email')]")
    if check_your_email_notification:
        return True
    else:
        return False

    assert check_your_email_notification.is_visible()

    context.close()
    browser.close()