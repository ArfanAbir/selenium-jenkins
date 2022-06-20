import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_031(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_031, self).__init__(driver)

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

    def showMetrics(self):
        wait = WebDriverWait(self.driver, 60)
        metrics = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@title='Show Metrics'])[1]")))
        self.driver.execute_script("arguments[0].click();", metrics)

    def volumeTab(self):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][normalize-space()='VOLUME'])[1]")))
        volume.click()

    def volRegularUncheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        reg = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Regular'])[2]")))
        self.driver.execute_script("arguments[0].click();", reg)

    def zoom1m(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        zoom = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][contains(text(),'1m')])[5]")))
        zoom.click()

    def volMidUncheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        mid = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Mid-Grade'])[2]")))
        mid.click()

    def volPremUncheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        prem = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Premium'])[2]")))
        self.driver.execute_script("arguments[0].click();", prem)

    def volDslUncheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        dsl = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Diesel'])[2]")))
        self.driver.execute_script("arguments[0].click();", dsl)

    def volRegularCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        reg = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Regular'])[2]")))
        self.driver.execute_script("arguments[0].click();", reg)

    def volMidCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        mid = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Mid-Grade'])[2]")))
        self.driver.execute_script("arguments[0].click();", mid)

    def volPremCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        prem = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Premium'])[2]")))
        self.driver.execute_script("arguments[0].click();", prem)

    def volDslCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        dsl = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Diesel'])[2]")))
        self.driver.execute_script("arguments[0].click();", dsl)