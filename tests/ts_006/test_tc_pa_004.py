import time

import allure

from Pages.ts_006_page.tc_pa_004 import tc_pa_004
from BasePage.BasePage import BasePage
from data.Credential import userData
email = userData.email
password = userData.password


class BPUSA_Home_Page(BasePage):
    @allure.step("FNO AI Rule")
    def test_tc_pa_004(self):
        tc_pa = tc_pa_004(self.driver)
        tc_pa.set_email(email)
        tc_pa.set_password(password)
        tc_pa.click_sign_in()
        tc_pa.selectState()
        tc_pa.selectStation()
        tc_pa.bulkAIRuleButton()
