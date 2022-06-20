import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_022(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_022, self).__init__(driver)

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

    def createPriceZone(self):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Create Pricing Zones'])[1]")))
        self.driver.execute_script("arguments[0].click();", volume)

    def stateSelection(self):
        wait = WebDriverWait(self.driver, 60)
        state = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='New York'])[1]")))
        self.driver.execute_script("arguments[0].click();", state)

    def openPriceCluster(self):
        wait = WebDriverWait(self.driver, 60)
        pcm = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='fixed-btn'])[1]")))
        self.driver.execute_script("arguments[0].click();", pcm)

    def closePriceCluster(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 60)
        pcm = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-angle-right cluster-price-close'])[1]")))
        self.driver.execute_script("arguments[0].click();", pcm)

    def checkSelectAll(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 60)
        pcm = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='checkAll'])[1]")))
        self.driver.execute_script("arguments[0].click();", pcm)

    def UncheckSelectAll(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 60)
        pcm = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='checkAll'])[1]")))
        self.driver.execute_script("arguments[0].click();", pcm)