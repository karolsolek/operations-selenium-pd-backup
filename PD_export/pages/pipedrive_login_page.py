from selenium.webdriver.common.by import By


class LoginPage:

    #region Selectors
    input_selector = "//input[@data-test='login']"
    password_selector = "//input[@data-test='password']"
    submit_button_selector = "submit"
    #endregion

    def __init__(self, browser):
        self.browser = browser

    #region Functions
    def log_in(self, login, password):
        login_input = self.browser.find_element(By.XPATH, LoginPage.input_selector)
        password_input = self.browser.find_element(By.XPATH, LoginPage.password_selector)
        login_button = self.browser.find_element(By.NAME, LoginPage.submit_button_selector)
        login_input.send_keys(login)
        password_input.send_keys(password)
        login_button.click()
    #endregion
