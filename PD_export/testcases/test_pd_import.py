import time
from PD_export.pages.pipedrive_login_page import LoginPage
from PD_export.pages.pipedrive_export_page import ExportPage
import pytest as pytest


@pytest.mark.usefixtures("setup")
class TestDemoName:
    def test_demo(self):
        lg = LoginPage(self.browser)
        ep = ExportPage(self.browser)
        lg.log_in("m.nowotynska@lexmotion.eu", "wXq8gMmp")
        time.sleep(4)
        ep.export_data()
        ep.export_leads()
        ep.export_deals()
        ep.export_organizations()
        ep.export_people()
        ep.export_products()
        ep.export_activities()
        ep.export_notes()

        ep.export_data_file()
        time.sleep(10)
