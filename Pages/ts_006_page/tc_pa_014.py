from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_014(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_014, self).__init__(driver)

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
        insights = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='navbarDropdown-analyatis']")))
        self.driver.execute_script("arguments[0].click();", insights)

    def metricsItem(self):
        wait = WebDriverWait(self.driver, 60)
        metrics = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Metrics'])[1]")))
        self.driver.execute_script("arguments[0].click();", metrics)

    def dateRange(self, dateRange):
        wait = WebDriverWait(self.driver, 60)
        date = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='txtEndDaterange'])[1]")))
        date.clear()
        date.send_keys(dateRange)

    def dateApply(self):
        wait = WebDriverWait(self.driver, 60)
        apply = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='applyBtn btn btn-sm btn-primary'])[1]")))
        apply.click()

    def productType(self):
        wait = WebDriverWait(self.driver, 60)
        product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@title='REGULAR'])[1]")))
        product.click()

    def productSelect(self):
        wait = WebDriverWait(self.driver, 60)
        product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[normalize-space()='REGULAR'])[1]")))
        product.click()

    def timeFormat(self):
        wait = WebDriverWait(self.driver, 60)
        time = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='ddlperiod'])[1]")))
        time.click()

    def timeSelect(self):
        wait = WebDriverWait(self.driver, 60)
        time = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='W']")))
        time.click()

    def state(self):
        wait = WebDriverWait(self.driver, 60)
        state = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@role='presentation'])[71]")))
        state.click()

    def submitButton(self):
        wait = WebDriverWait(self.driver, 60)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='btnsubmit'])[1]")))
        submit.click()
