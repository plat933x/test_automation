from selenium import webdriver
from selenium.webdriver.common.by import By
import time, datetime

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.southwest.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_xpath('//*[@id="LandingAirBookingSearchForm_originationAirportCode"]').send_keys("MSY")
        # Find departing field
        #time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="LandingAirBookingSearchForm_destinationAirportCode"]').send_keys("BUR")
        calendar1 = driver.find_element(By.XPATH, '//*[@id="LandingAirBookingSearchForm_departureDate"]').click()
        #calendar1 = driver.find_element_by_class_name("calendar-month--days")
        driver.find_element(By.XPATH, '//button[@id="calendar-112-2020-02-25"]').click()
        time.sleep(2)
        calendar2 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_returnDate').click()
        driver.find_element(By.ID, 'calendar-115-2020-03-13').click()
        #time.sleep(3)
        select_list = driver.find_element(By.XPATH, '//*[@class="flyout-trigger list-box"]')
        select_list.click()
        time.sleep(2)
        passenger_number = driver.find_element(By.XPATH, '//li[@id="LandingAirBookingSearchForm_adultPassengersCount--item-6"]')
        passenger_number.click()
        time.sleep(2)
        search = driver.find_element(By.ID, 'LandingAirBookingSearchForm_submit-button').click()

        #driver.quit()

print(datetime.datetime.now())
ff = CalendarSelection()
ff.test1()