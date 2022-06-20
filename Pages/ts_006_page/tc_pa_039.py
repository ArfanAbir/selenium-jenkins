import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_039(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_039, self).__init__(driver)

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

    def showMetrics(self):
        wait = WebDriverWait(self.driver, 60)
        metrics = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@title='Show Competitors Map'])[1]")))
        self.driver.execute_script("arguments[0].click();", metrics)

    def regCheck(self):
        wait = WebDriverWait(self.driver, 60)
        reg = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fa fa-circle'])[1]")))
        self.driver.execute_script("arguments[0].click();", reg)

    def midCheck(self):
        wait = WebDriverWait(self.driver, 60)
        mid = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fa fa-circle'])[2]")))
        self.driver.execute_script("arguments[0].click();", mid)

    def premCheck(self):
        wait = WebDriverWait(self.driver, 60)
        prem = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fa fa-circle'])[3]")))
        self.driver.execute_script("arguments[0].click();", prem)

    def dslCheck(self):
        wait = WebDriverWait(self.driver, 60)
        dsl = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fa fa-circle'])[4]")))
        self.driver.execute_script("arguments[0].click();", dsl)