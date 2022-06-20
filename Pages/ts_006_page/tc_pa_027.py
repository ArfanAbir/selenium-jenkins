import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_027(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_027, self).__init__(driver)

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

    def timeFormat(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        timez = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div/div/table/tbody[3]/tr/td/div[1]/div/div[1]/div/select")))
        self.driver.execute_script("arguments[0].click();", timez)

    def timeDay(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        day = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='Days']")))
        self.driver.execute_script("arguments[0].click();", day)

    def showMetrics(self):
        wait = WebDriverWait(self.driver, 60)
        metrics = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@title='Show Metrics'])[1]")))
        self.driver.execute_script("arguments[0].click();", metrics)

    def marginFuel(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        margin = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][@class='highcharts-title'])[12]")))
        margin.click()

    def zoom1m(self):
        wait = WebDriverWait(self.driver, 60)
        zoom1m = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][contains(text(),'1m')])[1]")))
        zoom1m.click()

    def regProduct(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 120)
        product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='mmfch active'][normalize-space()='REG'])[1]")))
        self.driver.execute_script("arguments[0].click();", product)

    def regMarginalUncheck(self):
        wait = WebDriverWait(self.driver, 60)
        regMarginal = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show REG Margin Fuel'])[1]")))
        self.driver.execute_script("arguments[0].click();", regMarginal)

    def regMarginalCheck(self):
        wait = WebDriverWait(self.driver, 60)
        regMarginal = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show REG Margin Fuel'])[1]")))
        self.driver.execute_script("arguments[0].click();", regMarginal)

    def cpgUncheck(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        cpg = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show CPG']")))
        cpg.click()

    def cpgCheck(self):
        wait = WebDriverWait(self.driver, 60)
        cpg = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show CPG']")))
        cpg.click()