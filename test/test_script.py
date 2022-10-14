import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions as SeleniumExceptions
import time

import selenium_utils as SU


@pytest.fixture(scope = "module")
def driver():
    # The URL to the web app.
    l_url = "https://factorial-php.azurewebsites.net"
    #l_url = "https://factorialcalculator.azurewebsites.net"

    # Options for the browser.
    l_chrome_options = webdriver.ChromeOptions()

    # Set option to remove the 'automation' banner at the top of the screen.
    l_chrome_options.add_experimental_option("useAutomationExtension", False)
    l_chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

    l_chrome_options.add_argument("--headless")

    # The web driver.
    l_driver = webdriver.Chrome(chrome_options = l_chrome_options)

    # Go to web application's page.
    l_driver.set_page_load_timeout(10)
    while True:
        try:
            l_driver.get(l_url)
        except SeleniumExceptions.TimeoutException:
            continue

        break

    l_driver.maximize_window()

    yield l_driver

    l_driver.close()

@pytest.fixture(scope = "module")
def xpath_txt_factorial():
    return "//input[@id='txtNumber']"

@pytest.fixture(scope = "module")
def xpath_btn_calculate():
    return "//input[@type='submit']"


def test_empty_input(driver, xpath_txt_factorial, xpath_btn_calculate):

    # The textbox into which the user can input the number whose factorial they wish to calculate.
    #l_txt_factorial = SU.GetElement(pytest.driver, By.XPATH, xpath_txt_factorial)

    # Enter the number into the textbox.
    #l_txt_factorial.send_keys("5")
    time.sleep(2)

    # Click the button that submit the form.
    SU.Click(driver, By.XPATH, xpath_btn_calculate)
    time.sleep(2)

    # Print the result.
    l_result = SU.GetElementText(driver, By.XPATH, "//p")
    time.sleep(2)

    driver.back()
    time.sleep(2)

    assert l_result == "Please enter a positive integer."

def test_0(driver, xpath_txt_factorial, xpath_btn_calculate):

    # The textbox into which the user can input the number whose factorial they wish to calculate.
    l_txt_factorial = SU.GetElement(driver, By.XPATH, xpath_txt_factorial)

    # Enter the number into the textbox.
    l_txt_factorial.send_keys("0")
    time.sleep(2)

    # Click the button that submit the form.
    SU.Click(driver, By.XPATH, xpath_btn_calculate)
    time.sleep(2)

    # Print the result.
    l_result = SU.GetElementText(driver, By.XPATH, "//p")
    time.sleep(2)

    driver.back()
    time.sleep(2)

    assert l_result == "0! is 1."