import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_043(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_043, self).__init__(driver)

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

    def statusFilter(self):
        wait = WebDriverWait(self.driver, 60)
        name = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='status_filter']")))
        name.click()

    def clearFilter(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        name = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='m-clear-table']")))
        name.click()

    def reviewPrice(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        name = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Review Price']")))
        name.click()

    def publish(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        name = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Published']")))
        name.click()

    def implemented(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        name = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Implemented']")))
        name.click()

    def selectAll(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Select All'])[1]")))
        name.click()

    def searchBar(self, value):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='m-search-table']")))
        search.send_keys(value)

    def applyButton(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        apply = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='m-ok-table']")))
        apply.click()

