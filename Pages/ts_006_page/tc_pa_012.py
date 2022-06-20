from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_012(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_012, self).__init__(driver)

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

    def selectStation(self):
        wait = WebDriverWait(self.driver, 60)
        station = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='m-sall-table']")))
        station.click()

    def filterIcon(self):
        wait = WebDriverWait(self.driver, 60)
        icon = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@id='station_filter'])[1]")))
        icon.click()

    def clearStation(self):
        wait = WebDriverWait(self.driver, 60)
        selectAll = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Clear'])[1]")))
        selectAll.click()

    def okayButton(self):
        wait = WebDriverWait(self.driver, 60)
        ok = wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[normalize-space()='Ok'])[1]")))
        ok.click()