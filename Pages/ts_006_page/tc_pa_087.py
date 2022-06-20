import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_087(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_087, self).__init__(driver)

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
                                              "//ul[@id='manager-station']//span[@class='statesName tradeclusters'][normalize-space()='New York']")))
        station.click()

    def stationManager(self):
        wait = WebDriverWait(self.driver, 60)
        manager = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='SURVEY']")))
        self.driver.execute_script("arguments[0].click();", manager)

    def showCompetitorMap(self):
        wait = WebDriverWait(self.driver, 120)
        competitor = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@title='Show Competitors Map'])[1]")))
        self.driver.execute_script("arguments[0].click();", competitor)

    def actionFilter(self):
        wait = WebDriverWait(self.driver, 60)
        filterIcon = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='filter-option-inner'])[3]")))
        filterIcon.click()

    def notPublished(self):
        wait = WebDriverWait(self.driver, 60)
        filterItem = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Not Published']")))
        filterItem.click()

    def implemented(self):
        wait = WebDriverWait(self.driver, 60)
        filterItem = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Implemented']")))
        filterItem.click()

    def tobeImplemented(self):
        wait = WebDriverWait(self.driver, 60)
        filterItem = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='To be Implemented']")))
        filterItem.click()

    def notPublishedAgain(self):
        wait = WebDriverWait(self.driver, 60)
        filterItem = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Not Published']")))
        filterItem.click()

    def implementedAgain(self):
        wait = WebDriverWait(self.driver, 60)
        filterItem = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Implemented']")))
        filterItem.click()

    def tobeImplementedAgain(self):
        wait = WebDriverWait(self.driver, 60)
        filterItem = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='To be Implemented']")))
        filterItem.click()

    def midGradeData(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        mid = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='MID-GRADE']//i[@class='fa fa-circle']")))
        mid.click()

    def premData(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        prem = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='PREMUM']//i[@class='fa fa-circle']")))
        prem.click()

    def dslData(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        dsl = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='DIESEL']//i[@class='fa fa-circle']")))
        dsl.click()

    def regData(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        reg = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='REGULAR']//i[@class='fa fa-circle']")))
        reg.click()
