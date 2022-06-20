import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_040(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_040,self).__init__(driver)

    def set_email(self, email):
        wait = WebDriverWait(self.driver, 60)
        loginEmail = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='txtemail']")))
        loginEmail.send_keys(email)

    def set_password(self, password):
        wait = WebDriverWait(self.driver, 60)
        loginEmail = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='txtpassword']")))
        loginEmail.send_keys(password)

    def click_sign_in(self):
        wait = WebDriverWait(self.driver, 60)
        loginEmail = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='btnsubmit']")))
        loginEmail.click()

    def selectState(self):
        wait = WebDriverWait(self.driver, 60)
        station = wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//ul[@id='treePricing']//ul[@id='treePricing']//span[@class='statesName tradeclusters'][normalize-space()='New York']")))
        station.click()

    def stationManager(self):
        wait = WebDriverWait(self.driver, 60)
        manager = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@target='_blank'])[1]")))
        self.driver.execute_script("arguments[0].click();", manager)

    def switchTab(self):
        handle_parent = self.driver.current_window_handle
        print(handle_parent)
        handles = self.driver.window_handles

        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.current_url)

            if self.driver.current_url == "https://bpusa.zdaly.com/Home":
                self.driver.close()

    def settingIcon(self):
        wait = WebDriverWait(self.driver, 60)
        metrics = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@title='Show Survey Management']")))
        self.driver.execute_script("arguments[0].click();", metrics)

    def createSurvey(self):
        wait = WebDriverWait(self.driver, 60)
        create = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn pub-btn pull-right']")))
        self.driver.execute_script("arguments[0].click();", create)

    def regVolume(self, value):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputSurveyRegVolume']")))
        volume.send_keys(value)

    def midVolume(self, value):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputSurveyMidVolume']")))
        volume.send_keys(value)

    def premVolume(self, value):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputSurveyPremVolume']")))
        volume.send_keys(value)

    def dslVolume(self, value):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputSurveyDslVolume']")))
        volume.send_keys(value)

    def scrollDown(self):
        wait = WebDriverWait(self.driver, 60)
        scrollPoint = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btnSurveySubmit']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", scrollPoint)

    def submitBtn(self):
        wait = WebDriverWait(self.driver, 60)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btnSurveySubmit']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)