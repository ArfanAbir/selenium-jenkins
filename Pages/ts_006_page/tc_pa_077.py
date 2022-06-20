import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_077(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_077, self).__init__(driver)

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

    def scrollDown(self):
        wait = WebDriverWait(self.driver, 60)
        scrollPoint = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//th[normalize-space()='premium']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", scrollPoint)

    def impactButton(self):
        wait = WebDriverWait(self.driver, 60)
        impact = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'I')])[8]")))
        impact.click()

    def closeButton(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        close = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='×']")))
        self.driver.execute_script("arguments[0].click();", close)