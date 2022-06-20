from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_027(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_027, self).__init__(driver)

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

    def selectStation(self):
        wait = WebDriverWait(self.driver, 60)
        newYork = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='checkbox'])[11]")))
        newYork.click()

    def selectState(self):
        wait = WebDriverWait(self.driver, 60)
        station = wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//ul[@id='treePricing']//ul[@id='treePricing']//span[@class='statesName tradeclusters'][normalize-space()='New York']")))
        station.click()

    def aiAnalyzer(self):
        wait = WebDriverWait(self.driver, 60)
        analyzer = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='btnCurrentai']")))
        analyzer.click()

    def newRole(self):
        wait = WebDriverWait(self.driver, 60)
        role = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='addNewRule']")))
        role.click()

    def roleName(self, role):
        wait = WebDriverWait(self.driver, 60)
        roleName = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='rulename']")))
        roleName.send_keys(role)

    def selectProductDropDown(self):
        wait = WebDriverWait(self.driver, 60)
        product = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='ruleform']/div/div/div[1]/div[2]/div[1]/div/span/div/button")))
        product.click()

    def selectProduct(self):
        wait = WebDriverWait(self.driver, 60)
        reg = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='ruleform']/div/div/div[1]/div[2]/div[1]/div/span/div/ul/li[3]/a/label")))
        reg.click()

    def creditType(self):
        wait = WebDriverWait(self.driver, 60)
        credit = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='ruleform']/div/div/div[1]/div[2]/div[2]/div/label[1]")))
        credit.click()

    def referenceType(self):
        wait = WebDriverWait(self.driver, 60)
        competetor = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[2]/div/span/div/button')))
        competetor.click()

    def competetorType(self):
        wait = WebDriverWait(self.driver, 60)
        type = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[3]/div/span/div/button')))
        type.click()

    def competetorTypeSelect(self):
        wait = WebDriverWait(self.driver, 60)
        type = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[3]/div/span/div/ul/li[2]/a/label')))
        type.click()

    def refProduct(self):
        wait = WebDriverWait(self.driver, 60)
        product = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[4]/div/span/div/button')))
        product.click()

    def refProductSelect(self):
        wait = WebDriverWait(self.driver, 60)
        product = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[4]/div/span/div/ul/li[5]/a/label')))
        product.click()

    def referenceCalculation(self):
        wait = WebDriverWait(self.driver, 60)
        calc = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[5]/div/span/div/button')))
        calc.click()

    def referenceCalcType(self):
        wait = WebDriverWait(self.driver, 60)
        calc = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[5]/div/span/div/ul/li[4]/a/label')))
        calc.click()

    def plusIcon(self):
        wait = WebDriverWait(self.driver, 60)
        plus = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[7]/div/label[1]')))
        plus.click()

    def value(self, val):
        wait = WebDriverWait(self.driver, 60)
        value = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='rulevalue']")))
        value.send_keys(val)

    def testStartDate(self, date):
        wait = WebDriverWait(self.driver, 60)
        startDate = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='rulestarttest']")))
        startDate.send_keys(date)
        # out = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[12]')))
        # out.click()

    def testEndDate(self, date):
        wait = WebDriverWait(self.driver, 60)
        endDate = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='ruleendtest']")))
        endDate.send_keys(date)
        # out = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ruleform"]/div/div/div[12]')))
        # out.click()

    def test(self):
        wait = WebDriverWait(self.driver, 60)
        test = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='testrule']")))
        test.click()

    def checkTest(self):
        wait = WebDriverWait(self.driver, 60)
        test = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[@id='testchart'])[1]")))
        if test.is_displayed:
            print("Test is Passed")
        else:
            test.click()

