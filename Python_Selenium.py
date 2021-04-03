import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.implicitly_wait(10)


def open_browser(url):
    driver.get(url)


def start_city(keyword, start_airport):
    driver.find_element_by_xpath("//*[@id='em__b-UID__booking-journeyType-ow']").click()
    driver.find_element_by_xpath("//*[@id='em__b-UID__booking-origin']").send_keys(keyword)
    driver.find_element_by_xpath("//*[contains(text(), '" + start_airport + "')]").click()


def destination_city(shortword, des_airport):
    driver.find_element_by_xpath("//*[@id='em__b-UID__booking-destination']").send_keys(shortword)
    driver.find_element_by_xpath("//*[contains(text(),'" + des_airport + "')]").click()


def date(pick_date):
    driver.find_element_by_xpath("//*[@id='em__b-UID__booking-departure']").click()
    calendar = driver.find_element_by_xpath("//*[@id='desktop-datepicker-container']")
    driver.SwitchTo(calendar)
    driver.find_element_by_xpath("//*[@aria-label='" + pick_date + "']").click()


def tickets(tickets_number, age):
    driver.find_element_by_xpath("//*[@id='em__b-UID__booking-travelers']").click()
    driver.implicitly_wait(50)
    driver.find_element_by_xpath("//*[@id='" + age + "']").click()
    for i in range(0, tickets_number):
        driver.find_element_by_xpath("//button[@class='TravelerSelector__poperIncrement']").click()
        driver.implicitly_wait(50)
        i += 1
    driver.find_element_by_xpath("//*[@class='Booking_submitButton']").click()
    time.sleep(10)


def close_browser(title):
    page = driver.current_window_handle
    assert title in driver.title
    time.sleep(5)
    driver.quit()


# Test Script:
open_browser(url="https://www.xxxxx.com/en-ca/great-fares-xxx")
start_city(keyword="Tor", start_airport='Toronto-Pearson')
destination_city(shortword="sha", des_airport='PVG xxxx Int')
date(pick_date='Sat Apr 17, 2021')
tickets(tickets_number=3, age='age1')
close_browser(title="Air xxxx - Select flights")
