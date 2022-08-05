from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def log_in(self, login, password):
        login_input = self.browser.find_element(By.XPATH, " //input[@data-test='login']")
        password_input = self.browser.find_element(By.XPATH, " //input[@data-test='password']")
        login_button = self.browser.find_element(By.NAME, "submit")
        login_input.send_keys(login)
        password_input.send_keys(password)
        login_button.click()
