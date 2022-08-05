from selenium.webdriver.common.by import By
import time


class ExportPage:

    def __init__(self, browser):
        self.browser = browser

    def export_data(self, button_name):
        self.browser.get('https://lexmotion.pipedrive.com/settings/export')
        time.sleep(4)
        iframe = self.browser.find_element(By.XPATH, "//iframe[@id='iFrameResizer0']")
        self.browser.switch_to.frame(iframe)

        # match button_name:
            # case Leads:
        csv_button = self.browser.find_element(By.XPATH, "//button[@id='do-export-csv']")
        csv_button.click()

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
        return "https://lexmotion.pipedrive.com/export/download/"+ last_record_number[0:3]


    def get_export_file(self):
        time.sleep(20)
        self.browser.get(self.build_url())