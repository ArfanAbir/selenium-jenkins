import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_094(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_094, self).__init__(driver)

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
        manager = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='SURVEY']")))
        self.driver.execute_script("arguments[0].click();", manager)

    def messageIcon(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        message = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Messaging']")))
        self.driver.execute_script("arguments[0].click();", message)

    def markasRead(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        message = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fa fa-envelope-open isread'])[1]")))
        self.driver.execute_script("arguments[0].click();", message)

    def deleteMessage(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        delete = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class,'fa fa-trash isremove')])[1]")))
        self.driver.execute_script("arguments[0].click();", delete)

    def deleteCancel(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        delete = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='cancel']")))
        self.driver.execute_script("arguments[0].click();", delete)
