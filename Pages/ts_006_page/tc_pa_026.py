import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_026(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_026, self).__init__(driver)

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

    def clusterInsights(self):
        wait = WebDriverWait(self.driver, 60)
        cluster = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@title='Cluster Insight'])[1]")))
        self.driver.execute_script("arguments[0].click();", cluster)

    def switchTab(self):
        handle_parent = self.driver.current_window_handle
        print(handle_parent)
        handles = self.driver.window_handles

        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.current_url)

            if self.driver.current_url == "https://bpusa.zdaly.com/Home":
                self.driver.close()

    def zoom1m(self):
        wait = WebDriverWait(self.driver, 60)
        zoom1m = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][normalize-space()='1m'])[1]")))
        zoom1m.click()

    def positionBrand(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        scrollPoint = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Price Position of Brands']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", scrollPoint)

    def currentDiff(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        diff = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='currentDiff']")))
        self.driver.execute_script("arguments[0].click();", diff)

    def competitorsInCluster(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        comp = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Competitors in Cluster']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", comp)

    def stationPositionComp(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        comp = wait.until(EC.element_to_be_clickable((By.XPATH, "(//p[@class='chart-heading v2'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", comp)