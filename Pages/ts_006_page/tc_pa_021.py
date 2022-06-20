import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_021(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_021, self).__init__(driver)

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

    def volumeDecomposition(self):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Volume Decomposition'])[1]")))
        self.driver.execute_script("arguments[0].click();", volume)

    def startDate(self, startDate):
        wait = WebDriverWait(self.driver, 60)
        start = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='txtStartDate'])[1]")))
        start.clear()
        start.send_keys(startDate)

    def endDate(self, endDate):
        wait = WebDriverWait(self.driver, 60)
        end = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='txtEndDate'])[1]")))
        end.clear()
        end.send_keys(endDate)

    def stateSelect(self):
        wait = WebDriverWait(self.driver, 60)
        state = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='New York']")))
        self.driver.execute_script("arguments[0].click();", state)

    def applyButton(self):
        wait = WebDriverWait(self.driver, 60)
        apply = wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[normalize-space()='Apply'])[1]")))
        apply.click()

    def exitChart(self):
        wait = WebDriverWait(self.driver, 60)
        state = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-times'])[1]")))
        self.driver.execute_script("arguments[0].click();", state)

    def switchLight(self):
        wait = WebDriverWait(self.driver, 60)
        light = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='switchTextL']")))
        self.driver.execute_script("arguments[0].click();", light)

    def advanceArea(self):
        wait = WebDriverWait(self.driver, 60)
        advance = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-chart-area'])[1]")))
        self.driver.execute_script("arguments[0].click();", advance)

