import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_023(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_023, self).__init__(driver)

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

    def insightsIcon(self):
        wait = WebDriverWait(self.driver, 60)
        insights = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='navbarDropdown-analyatis']")))
        self.driver.execute_script("arguments[0].click();", insights)

    def portfolioAnalyzer(self):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Portfolio and Competitor Analyzer'])[1]")))
        self.driver.execute_script("arguments[0].click();", volume)

    def stateSelection(self):
        wait = WebDriverWait(self.driver, 60)
        state = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//span[normalize-space()='New York'])[1]")))
        self.driver.execute_script("arguments[0].click();", state)

    def uncheckSelectAll(self):
        wait = WebDriverWait(self.driver, 180)
        uncheck = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='checkAll'])[1]")))
        self.driver.execute_script("arguments[0].click();", uncheck)

    def checkSelectAll(self):
        wait = WebDriverWait(self.driver, 180)
        uncheck = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='checkAll'])[1]")))
        self.driver.execute_script("arguments[0].click();", uncheck)

    def stationSelect(self):
        wait = WebDriverWait(self.driver, 60)
        station = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mapbox"]/div[9]/a[2770]')))
        self.driver.execute_script("arguments[0].click();", station)