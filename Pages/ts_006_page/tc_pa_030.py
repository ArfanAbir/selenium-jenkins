import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_030(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_030, self).__init__(driver)

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

    def timeFormat(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        timez = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[2]/div/div/table/tbody[3]/tr/td/div[1]/div/div[1]/div/select")))
        timez.click()

    def timeWeek(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        week = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='Weekly']")))
        week.click()

    def timeSubmit(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnsubmit']")))
        submit.click()

    def revNonFuel(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        swipe = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][@class='highcharts-title'])[15]")))
        swipe.click()

    def NonrevZoom1m(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        zoom = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][contains(text(),'6m')])[4]")))
        zoom.click()

    def NonRevRevenueUncheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        revenue = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Revenue'])[1]")))
        self.driver.execute_script("arguments[0].click();", revenue)

    def NonRevRevenueCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        revenue = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Show Revenue'])[1]")))
        self.driver.execute_script("arguments[0].click();", revenue)