from selenium.webdriver.common.by import By
import time


class ExportPage:

    def __init__(self, browser):
        self.browser = browser

    def export_data(self):
        self.browser.get('https://lexmotion.pipedrive.com/settings/export')
        time.sleep(4)
        iframe = self.browser.find_element(By.XPATH, "//iframe[@id='iFrameResizer0']")
        self.browser.switch_to.frame(iframe)
       # global data_type_buttons
       # data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
       # global csv_button
       # csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")

        # match button_name:
        # case Leads:

        # data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
        # data_type_buttons[0].click()

        # csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        # csv_button.click()

    # xls_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-xls']")
    # xls_button.click()

    def build_url(self):
        time.sleep(4)
        all_files = self.browser.find_elements(By.XPATH, "//table[@id='exports_list']//tr")
        last_record = all_files.pop()
        last_record_number = last_record.text
        return "https://lexmotion.pipedrive.com/export/download/" + last_record_number[0:3]

    def build_data_type_buttons_selector(self):
        time.sleep(4)
        iframe = self.browser.find_element(By.XPATH, "//iframe[@id='iFrameResizer0']")
        self.browser.switch_to.frame(iframe)
      #  frame = self.browser.find_element(By.XPATH, "//div[@class='row nolabel export-data-items']")
       # self.browser.switch_to.frame(frame)
        data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
        return data_type_buttons

    def export_data_file(self):
        time.sleep(2)
        self.browser.get(self.build_url())

    def export_leads(self):
        csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        csv_button.click()
        self.export_data_file()

    def export_deals(self):
       # data_type_button = self.build_data_type_buttons_selector()
       iframe = self.browser.find_element(By.XPATH, "//iframe[@id='iFrameResizer0']")
       self.browser.switch_to.frame(iframe)
       data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
       data_type_buttons[0].click()
       csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
       csv_button.click()
       self.export_data_file()

    def export_organizations(self):
        data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
        data_type_buttons[1].click()
        csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        csv_button.click()

    def export_people(self):
        data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
        data_type_buttons[2].click()
        csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        csv_button.click()

    def export_products(self):
        data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
        data_type_buttons[3].click()
        csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        csv_button.click()

    def export_activities(self):
        data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
        data_type_buttons[4].click()
        csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        csv_button.click()

    def export_notes(self):
        data_type_buttons = self.browser.find_elements(By.XPATH, "//label[@class='fancy_radio inline']")
        data_type_buttons[5].click()
        csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        csv_button.click()