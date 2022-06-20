import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_089(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_089, self).__init__(driver)

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

    def userProfile(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 60)
        profile = wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@src='/Content/img/user.png'])[1]")))
        self.driver.execute_script("arguments[0].click();", profile)

    def userSetting(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Settings']")))
        self.driver.execute_script("arguments[0].click();", setting)

    def brandName(self, name):
        wait = WebDriverWait(self.driver, 60)
        settingName = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='brand'])[1]")))
        settingName.clear()
        settingName.send_keys(name)

    def priceFormat(self):
        wait = WebDriverWait(self.driver, 60)
        price = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select)[2]")))
        price.click()

    def priceFormatType(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        price = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-settings"]/fieldset/div[2]/div/select/option[2]')))
        self.driver.execute_script("arguments[0].click();", price)

    def priceTypeDrop(self):
        wait = WebDriverWait(self.driver, 60)
        price = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@class='form-control'])[2]")))
        price.click()

    def priceTypeItem(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        price = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='credit']")))
        price.click()

    def passwordManagerDrop(self):
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@class='form-control'])[3]")))
        password.click()

    def passwordManagerItem(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-settings"]/fieldset/div[4]/div/select/option[1]')))
        password.click()

    def available(self):
        wait = WebDriverWait(self.driver, 60)
        available = wait.until(EC.visibility_of_element_located((By.XPATH, "(//label[normalize-space()='Available Pages'])[1]")))
        available.click()

    def availPagesDrop(self):
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-settings"]/fieldset/div[5]/div/div/button')))
        password.click()

    def availPagesItem(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][normalize-space()='Select All'])[1]")))
        password.click()

    def defaultPageDrop(self):
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@title='Nothing selected'])[1]")))
        password.click()

    def defaultPageItem(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Price Analyst/Station Manager'])[1]")))
        password.click()

    def availableReportsDrop(self):
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='filter-option-inner-inner'])[3]")))
        password.click()

    def availableReportsItem(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@type,'button')][normalize-space()='Select All'])[2]")))
        password.click()

    def availableReports(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        ar = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Available Reports']")))
        ar.click()

    def incrementStep(self, name):
        wait = WebDriverWait(self.driver, 60)
        settingName = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'text')])[2]")))
        settingName.clear()
        settingName.send_keys(name)

    def regProduct(self):
        wait = WebDriverWait(self.driver, 60)
        reg = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[normalize-space()='REG'])[1]")))
        reg.click()

    def showStationManager(self):
        wait = WebDriverWait(self.driver, 60)
        station_manager = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@aria-label='...'])[1]")))
        station_manager.click()

    def showMetrics(self):
        wait = WebDriverWait(self.driver, 60)
        station_manager = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@aria-label,'...')])[2]")))
        station_manager.click()

    def showMap(self):
        wait = WebDriverWait(self.driver, 60)
        station_manager = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='blankCheckbox1'])[1]")))
        station_manager.click()

    def scrollDown(self):
        wait = WebDriverWait(self.driver, 60)
        scrollPoint = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//legend[normalize-space()='Price Analyst'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", scrollPoint)

    def opisTitle(self, title):
        wait = WebDriverWait(self.driver, 60)
        settingName = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='opis']")))
        settingName.clear()
        settingName.send_keys(title)

    def analystName(self):
        wait = WebDriverWait(self.driver, 60)
        station_manager = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@aria-label='...'])[4]")))
        station_manager.click()

    def submitButton(self):
        wait = WebDriverWait(self.driver, 60)
        station_manager = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@aria-label='...'])[4]")))
        station_manager.click()
