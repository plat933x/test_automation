import re, string, random, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CandyMapper:

    # Locators gathered for UI interactions with CandyMapper test webpage
    POP_UP_BUTTON = (By.XPATH, "//*[@id='popup-widget307423-close-icon']")
    IMAGE = (By.ID, "n-307293")
    HOME_TAB = (By.XPATH, "//*[contains(text(), 'Home')]")
    WELCOME_TEXT = (By.XPATH, "//span[contains(text(),'must be done')]")
    HALLOWEEN_PARTY_TAB = (By.XPATH, "//a[text() = 'Halloween Party']")
    HALLOWEEN_VERIFY = (By.XPATH, "//a[normalize-space()='I Am Hosting A Party']")
    MORE_DROPDOWN_LIST = (By.ID, "2")
    DROPDOWN = (By.ID, "more-24933")
    MAGIC_TAB = (By.XPATH, "//a[contains(text(),'Magic Object Model?')])[2]")
    FIND_MY_CANDY_TAB = (By.XPATH, "//h1[@id='8c2b2395-8a26-4133-a2d1-00c9f5d0031a]")
    VAMPIRA_IMAGE = (By.XPATH, "//*[@id='bs-6']/span/section/div/div/div[1]/main/div[2]/p[1]/figure/div/img")

    # CandyMapper address:
    URL = "https://candymapper.com/"

    def __init__(self, browser):
        self.browser = browser

    # Open URL method
    def open_url(self):
        try:
            self.browser.get(self.URL)
        except Exception as e:
            print("CandyMapper cannot be opened", e)

    def pop_up_button(self):
        pop_up = self.browser.find_element(*self.POP_UP_BUTTON)
        pop_up.click()
        return pop_up

    def open_candy_mapper(self):
        CandyMapper.open_url(self)
        CandyMapper.pop_up_button(self)

    def scroll_down(self, x="document.body.scrollHeight"):
        self.browser.execute_script(f"window.scrollTo(0,{x})")
        time.sleep(1)

    def go_to_home_tab(self):
        self.browser.find_element(*self.HOME_TAB).click()
        welcome_text = self.browser.find_element(*self.WELCOME_TEXT)
        if welcome_text:
            return True
        else:
            return False

    def is_image_visible(self):
        image = self.browser.find_element(*self.IMAGE)
        if image:
            return True
        else:
            return False

    def go_to_halloween_tab(self):
        self.browser.find_element(*self.HALLOWEEN_PARTY_TAB).click()
        halloween_tab_verify = self.browser.find_element(*self.HALLOWEEN_VERIFY)

        if halloween_tab_verify:
            return True
        else:
            return False

    def interact_with_more_list(self):
        more = self.browser.find_element(*self.MORE_DROPDOWN_LIST)
        more.click()
        return more

    def go_to_magic_tab(self):
        magic_tab = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='more-24933']/li[9]/a"))
        )
        magic_tab.click()
        time.sleep(1)

    def go_to_find_my_candy_tab(self):
        find_my_candy = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='more-24933']/li[6]/a"))
        )
        find_my_candy.click()
        time.sleep(1)

        find_candy_verify = self.browser.find_element(*self.FIND_MY_CANDY_TAB)
        if find_candy_verify:
            return True
        else:
            return False

    def vampira_blog_image(self):
        vampira_blog_image = self.browser.find_element(*self.VAMPIRA_IMAGE)
        if vampira_blog_image:
            return True
        else:
            return False