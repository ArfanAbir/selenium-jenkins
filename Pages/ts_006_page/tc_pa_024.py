import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_024(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_024, self).__init__(driver)

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

    def businessDriver(self):
        wait = WebDriverWait(self.driver, 60)
        volume = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Business Drivers'])[1]")))
        self.driver.execute_script("arguments[0].click();", volume)

    def stateSelection(self):
        wait = WebDriverWait(self.driver, 60)
        state = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//span[normalize-space()='New York'])[1]")))
        self.driver.execute_script("arguments[0].click();", state)

    def productDropdown(self):
        wait = WebDriverWait(self.driver, 60)
        drop = wait.until(EC.visibility_of_element_located((By.XPATH, "(//select[@id='product-type'])[1]")))
        self.driver.execute_script("arguments[0].click();", drop)

    def productSelect(self):
        wait = WebDriverWait(self.driver, 60)
        product = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='product-type']/option[1]")))
        self.driver.execute_script("arguments[0].click();", product)

    def applyButton(self):
        wait = WebDriverWait(self.driver, 60)
        product = wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[normalize-space()='Apply'])[1]")))
        self.driver.execute_script("arguments[0].click();", product)

    def summery(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        summery = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Summary'])[1]")))
        self.driver.execute_script("arguments[0].click();", summery)

    def factors(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        fact = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Factors'])[1]")))
        self.driver.execute_script("arguments[0].click();", fact)

    def seasonality(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        season = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Seasonality'])[1]")))
        self.driver.execute_script("arguments[0].click();", season)

    def weatherHoliday(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        weather = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Holiday & Weather Effects'])[1]")))
        self.driver.execute_script("arguments[0].click();", weather)

    def intradayEffect(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        intraday = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Intraday Effects'])[1]")))
        self.driver.execute_script("arguments[0].click();", intraday)

    def hideAdvanceOptions(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        hide = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-angle-double-right'])[1]")))
        self.driver.execute_script("arguments[0].click();", hide)

    def UnhideAdvanceOptions(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        hide = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-angle-double-left'])[1]")))
        self.driver.execute_script("arguments[0].click();", hide)

