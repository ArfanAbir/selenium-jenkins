import time

import allure

from Pages.ts_007_page.tc_pa_006 import TC_PA_006
from BasePage.BasePage import BasePage
from data.Credential import userData
email = userData.email
password = userData.password


class AIAnalyzer(BasePage):
    @allure.step("FNO Login into bpusa website")
    def test_tc_pa_006(self):
        tc_pa = TC_PA_006(self.driver)
        tc_pa.set_email(email)
        tc_pa.set_password(password)
        tc_pa.click_sign_in()
        tc_pa.selectState()
        tc_pa.selectStation()
        tc_pa.aiAnalyzer()
        tc_pa.newRole()
        tc_pa.roleName("Role TC_PA_006")
        tc_pa.selectProductDropDown()
        tc_pa.selectProduct()
        tc_pa.creditType()
        tc_pa.referenceType()
        tc_pa.competetorType()
        tc_pa.competetorTypeSelect()
        tc_pa.refProduct()
        tc_pa.refProductSelect()
        tc_pa.referenceCalculation()
        tc_pa.referenceCalcType()
        tc_pa.plusIcon()
        tc_pa.value("15")
        tc_pa.testStartDate("04/01/2022")
        tc_pa.testEndDate("04/15/2022")
        tc_pa.test()
        # time.sleep(2)
        # tc_pa.checkTest()

