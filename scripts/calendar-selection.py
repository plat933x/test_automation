from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, datetime

class SouthWest():

    def choose_flight(self):
        baseUrl = "http://www.southwest.com"

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        # safe time for webpage loaded
        time.sleep(5)

        # departure airport
        depart = driver.find_element(By.XPATH, '//*[@id="LandingAirBookingSearchForm_originationAirportCode"]')
        depart.click()
        depart.send_keys("MSY")
        time.sleep(1)
        depart.send_keys(Keys.ENTER)

        # arrive airport
        arrive = driver.find_element(By.XPATH, '//*[@id="LandingAirBookingSearchForm_destinationAirportCode"]')
        arrive.click()
        arrive.send_keys("BUR")
        time.sleep(1)
        arrive.send_keys(Keys.ENTER)

        time.sleep(1)
        passenger_number = driver.find_element(By.XPATH, '//*[@id="passenger-selector--input"]')
        passenger_number.click()
        time.sleep(1.5)
        adults_add = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[4]/div/div/div/div/div[1]/ul/li[1]/div[2]/div/button[2]/span[1]/span')
        adults_add.click()
        adults_add.click()
        time.sleep(1.5)

        search = driver.find_element(By.XPATH, '//*[@id="LandingAirBookingSearchForm_submit-button"]')
        search.click()
        time.sleep(3)

        next_page = driver.find_element(By.XPATH, "//h1[contains(text(), 'Book a Flight')]")
        if next_page is not None:
            return True
        else:
            return False

        driver.quit()

print(datetime.datetime.now())
ff = SouthWest()
ff.choose_flight()
