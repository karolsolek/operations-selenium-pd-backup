import sys
import traceback

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def log_in(self, login, password):
        try:
            login_input = self.browser.find_element(By.XPATH, "//input[@id='login']")
            password_input = self.browser.find_element(By.XPATH, "//input[@id='password']")
            login_button = self.browser.find_element(By.XPATH, "//div[@class='login']//button")
            login_input.send_keys(login)
            password_input.send_keys(password)
            login_button.click()
        except NoSuchElementException:
            print('Wrong page, correct field cannot be found')
            sys.exit(1)
