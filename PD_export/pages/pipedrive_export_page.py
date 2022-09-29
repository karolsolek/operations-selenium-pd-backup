import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExportPage:
    iframe_selector = "//iframe[@id='iFrameResizer0']"
    data_type_buttons_selector = "//label[@class='fancy_radio inline']"
    csv_button_selector = "//button[@id='do-export-csv']"

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 360)

    def export_data(self):
        self.browser.get('https://lexmotion.pipedrive.com/settings/export')
        time.sleep(4)
        iframe = self.browser.find_element(By.XPATH, ExportPage.iframe_selector)
        self.browser.switch_to.frame(iframe)

    def build_download_url(self, function_name):
        time.sleep(4)
        all_files = self.browser.find_elements(By.XPATH, "//table[@id='exports_list']//tr")
        last_record = all_files.pop()
        last_record_number = last_record.text
        if last_record_number.find("Failed") != -1:
            eval(function_name + "()")
        return "https://lexmotion.pipedrive.com/export/download/" + last_record_number[0:3]


    def build_download_status_selector(self):
        time.sleep(4)
        all_files = self.browser.find_elements(By.XPATH, "//table[@id='exports_list']//tr")
        last_record = all_files.pop()
        last_record_number = last_record.text
        return "https://lexmotion.pipedrive.com/export/download/" + last_record_number[0:3]

    def export_data_file(self, function_name):

        self.wait.until(EC.invisibility_of_element((By.XPATH, "//span[@class='spinner']")))
        self.browser.get(self.build_download_url(function_name))

    def export_leads(self):
        csv_button = self.browser.find_element(By.XPATH, ExportPage.csv_button_selector)
        csv_button.click()
        self.export_data_file("export_leads()")

    def export_deals(self):
        iframe = self.browser.find_element(By.XPATH, ExportPage.iframe_selector)
        self.browser.switch_to.frame(iframe)
        data_type_buttons = self.browser.find_elements(By.XPATH, ExportPage.data_type_buttons_selector)
        data_type_buttons[0].click()
        csv_button = self.browser.find_element(By.XPATH, ExportPage.csv_button_selector)
        csv_button.click()
        self.export_data_file(self, "export_deals")

    def export_organizations(self):
        iframe = self.browser.find_element(By.XPATH, ExportPage.iframe_selector)
        self.browser.switch_to.frame(iframe)
        data_type_buttons = self.browser.find_elements(By.XPATH, ExportPage.data_type_buttons_selector)
        data_type_buttons[1].click()
        csv_button = self.browser.find_element(By.XPATH, ExportPage.csv_button_selector)
        csv_button.click()
        self.export_data_file()

    def export_people(self):
        iframe = self.browser.find_element(By.XPATH, ExportPage.iframe_selector)
        self.browser.switch_to.frame(iframe)
        data_type_buttons = self.browser.find_elements(By.XPATH, ExportPage.data_type_buttons_selector)
        data_type_buttons[2].click()
        csv_button = self.browser.find_element(By.XPATH, ExportPage.csv_button_selector)
        csv_button.click()
        self.export_data_file()

    def export_products(self):
        iframe = self.browser.find_element(By.XPATH, ExportPage.iframe_selector)
        self.browser.switch_to.frame(iframe)
        data_type_buttons = self.browser.find_elements(By.XPATH, ExportPage.data_type_buttons_selector)
        data_type_buttons[3].click()
        csv_button = self.browser.find_element(By.XPATH, ExportPage.csv_button_selector)
        csv_button.click()
        self.export_data_file()

    def export_activities(self):
        iframe = self.browser.find_element(By.XPATH, ExportPage.iframe_selector)
        self.browser.switch_to.frame(iframe)
        data_type_buttons = self.browser.find_elements(By.XPATH, ExportPage.data_type_buttons_selector)
        data_type_buttons[4].click()
        csv_button = self.browser.find_element(By.XPATH, ExportPage.csv_button_selector)
        csv_button.click()
        self.export_data_file()

    def export_notes(self):
        iframe = self.browser.find_element(By.XPATH, ExportPage.iframe_selector)
        self.browser.switch_to.frame(iframe)
        data_type_buttons = self.browser.find_elements(By.XPATH, ExportPage.data_type_buttons_selector)
        data_type_buttons[5].click()
        csv_button = self.browser.find_element(By.XPATH, ExportPage.csv_button_selector)
        csv_button.click()
        self.export_data_file()
        time.sleep(60)
