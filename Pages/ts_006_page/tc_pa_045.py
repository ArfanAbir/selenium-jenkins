import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_045(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_045, self).__init__(driver)

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

    def creditFilter(self):
        wait = WebDriverWait(self.driver, 60)
        name = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@filter='credit_reg']")))
        name.click()

    def creditDropdown(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        drop = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@class='trewy']")))
        drop.click()

    def greaterThen(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        drop = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='m-list-table']/div/div[1]/select/option[1]")))
        self.driver.execute_script("arguments[0].click();", drop)

    def filterValue(self, value):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        drop = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='filter_maxval'])[1]")))
        drop.send_keys(value)

    def applyButton(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        apply = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='m-ok-table']")))
        apply.click()

