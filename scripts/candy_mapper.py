import re, string, random, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class CandyMapper:

    # Locators gathered for UI interactions with CandyMapper test webpage
    POP_UP_BUTTON = (By.XPATH, "//*[@id=\'popup-widget25042-cta']")
    IMAGE = (By.XPATH, "//*[@id='n-24920']/div/section/div[4]/div/div[2]/div/picture/img")
    HOME_TAB = (By.XPATH, "//*[contains(text(), 'Home')]")
    WELCOME_TEXT = (By.XPATH, "//span[contains(text(),'must be done')]")
    JOIN_US_TAB = (By.XPATH, "//a[text() = 'JOIN US']")
    JOINUS = (By.CSS_SELECTOR, "input[placeholder='Email']")
    HALLOWEEN_PARTY_TAB = (By.XPATH, "//a[text() = 'Halloween Party']")
    HALLOWEEN_VERIFY = (By.XPATH, "//a[normalize-space()='I Am Hosting A Party']")
    MORE_DROPDOWN_LIST = (By.CSS_SELECTOR, "a[id='2']")
    MAGIC_OBJECT_MODEL = (By.XPATH, "//a[@href='/magic-object-model%3F']")
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

    def go_to_joinus_tab(self):
        self.browser.find_element(*self.JOIN_US_TAB).click()
        joinus_tab = self.browser.find_element(*self.JOINUS)

        if joinus_tab:
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

    def click_on_more_dropdown_list(self):
        self.browser.find_element(*self.MORE_DROPDOWN_LIST).click()
        time.sleep(1)

    def go_to_magic_object_model(self):
        self.browser.find_element(*self.MAGIC_OBJECT_MODEL).click()
        time.sleep(1)