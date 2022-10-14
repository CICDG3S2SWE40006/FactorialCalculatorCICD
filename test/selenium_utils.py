'''
# Description:
    > This python script contains several functions that streamline the use of Selenium to scrape websites.

# Author/s:
    > Brett MacIsaac

# Composition:
    > Functions: 4

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as SeleniumExceptions
import time


# Functions (4) ========================================================================================================

'''
# Clicks a specified button on the website pointed to by the given web-driver object.

# Parameters:
    > a_driver: the web-driver that's currently on the website that contains the button that is to be pressed.
    > a_locater: an instance of the 'By' class which defines what is to be searched for (e.g. xpath, tag-name, id, etc).
    > a_string: the string that corresponds to a_locator.
    > a_length_wait: the length of time (s) that will be waited before the function 'times-out'. The dynamic elements of
                     a website might not yet exist when the function initially searches for them and, in the case of 
                     'clickable' elements, they might not yet be clickable; thus, it's favourable to wait a given length
                     of time before giving-up on the search.
    > a_print_text: a flag that, when true, indicates that the button's text is to be printed; if false, don't print it.
                    This can be useful for keeping track of a web-scraper's progress.

'''
def Click(a_driver, a_locator, a_string, a_length_wait = 10, a_print_text = False, a_x_offset = 0, a_y_offset = 0, a_pause = 0):

    if a_pause > 0:
        time.sleep(a_pause)

    while True:

        try:

            l_btn =  WebDriverWait(a_driver, a_length_wait).until(
                EC.element_to_be_clickable((a_locator, a_string))
            )

            # The button must be on the screen for it to be clicked (as is the case with any human user).
            if a_x_offset == 0 and a_y_offset == 0:
                a_driver.execute_script("arguments[0].scrollIntoView();", l_btn)
            else:
                a_driver.execute_script("window.scrollTo(arguments[0], arguments[1])", l_btn.location["x"] + a_x_offset, l_btn.location["y"] + a_y_offset)

            if a_print_text:

                print(l_btn.text)

            l_btn.click()

        except (SeleniumExceptions.ElementClickInterceptedException, SeleniumExceptions.StaleElementReferenceException):

            continue

        break

    if a_pause > 0:
        time.sleep(a_pause)


'''
# Retrieves and returns a specified list of elements from the website pointed to by the given web-driver object.

# Parameters:
    > a_driver: the web-driver that's currently on the website that contains the button that is to be pressed.
    > a_locater: an instance of the 'By' class which defines what is to be searched for (e.g. xpath, tag-name, id, etc).
    > a_string: the string that corresponds to a_locator
    > a_length_wait: the length of time (s) that will be waited before the function 'times-out'. The dynamic elements of
                     a website might not yet exist when the function initially searches for them; thus, it's favourable
                     to wait a given length of time before giving-up on the search.

'''
def GetElements(a_driver, a_locator, a_string, a_length_wait = 10):

    return WebDriverWait(a_driver, a_length_wait).until(
                EC.presence_of_all_elements_located((a_locator, a_string))
           )


'''
# Retrieves and returns a specified element from the website pointed to by the given web-driver object.

# Parameters:
    > a_driver: the web-driver that's currently on the website that contains the button that is to be pressed.
    > a_locater: an instance of the 'By' class which defines what is to be searched for (e.g. xpath, tag-name, id, etc).
    > a_string: the string that corresponds to a_locator
    > a_length_wait: the length of time (s) that will be waited before the function 'times-out'. The dynamic elements of
                     a website might not yet exist when the function initially searches for them; thus, it's favourable
                     to wait a given length of time before giving-up on the search.

'''
def GetElement(a_driver, a_locator, a_string, a_length_wait = 10):

    return  WebDriverWait(a_driver, a_length_wait).until(
                EC.presence_of_element_located((a_locator, a_string))
            )


'''
# Retrieves and returns the text of a specified element from the website pointed to by the given web-driver object.

# Parameters:
    > a_driver: the web-driver that's currently on the website that contains the button that is to be pressed.
    > a_locater: an instance of the 'By' class which defines what is to be searched for (e.g. xpath, tag-name, id, etc).
    > a_string: the string that corresponds to a_locator
    > a_length_wait: the length of time (s) that will be waited before the function 'times-out'. The dynamic elements of
                     a website might not yet exist when the function initially searches for them; thus, it's favourable
                     to wait a given length of time before giving-up on the search.

'''
def GetElementText(a_driver, a_locator, a_string, a_length_wait = 10):

    return WebDriverWait(a_driver, a_length_wait).until(
                EC.presence_of_element_located((a_locator, a_string))
           ).text