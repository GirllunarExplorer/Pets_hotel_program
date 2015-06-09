#!/usr/bin/env python
__author__ = 'tracyrohlin'

import requests, bs4
from selenium import webdriver
from pprint import pprint

def coupon(coupon_code):
    if len(coupon_code) != 19:
        raise Exception("Enter code surrounded by quotes, with space between each group")


    try:
        code = coupon_code.split()

        """web_page = requests.get("https://www.petsmartpetshotelsurvey.com/")
        web_page.raise_for_status()

        page_data = bs4.BeautifulSoup(web_page.text)
        first_box = page_data.find_all(id="CN1")
        for item in first_box:
            print item"""

        driver= webdriver.Firefox()
        driver.get("https://www.petsmartpetshotelsurvey.com/")
        first_box = driver.find_element_by_id("CN1")
        first_box.send_keys("", code[0])
        second_box = driver.find_element_by_id("CN2")
        second_box.send_keys("", code[1])
        third_box = driver.find_element_by_id("CN3")
        third_box.send_keys("", code[2])
        fourth_box = driver.find_element_by_id("CN4")
        fourth_box.send_keys("", code[3])

        hotel_option = driver.find_elements_by_xpath("//*[@type='radio' and @value='2']")[0]
        make_visible = driver.find_element_by_id("FIP")
        driver.execute_script("arguments[0].checked = true;", make_visible)
        hotel_option.click()
        print "I am done"
    except Exception as error:
        print error

print coupon("0520 1935 1575 6745")