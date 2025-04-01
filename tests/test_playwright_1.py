from playwright.sync_api import Playwright

def test_vampira_blog_content(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://candymapper.com/")

    page.locator("#popup-widget25042-cta").click()
    page.get_by_role("button", name="More").click()
    page.get_by_role("menuitem", name="Vampira's Blog").get_by_label("HomeJOIN USHalloween").click()
    page.get_by_role("button", name="Continue Reading").click()
    page.get_by_role("figure").get_by_role("img").wait_for(state="visible")

    current_url = page.url

    assert current_url == 'https://candymapper.com/vampiras-blog/f/candymapper-is-under-new-management-1', "Vampira's Blog has not been reached, wrong URL asserted."

    context.close()
    browser.close()
