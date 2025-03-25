from selenium.webdriver.common.by import By

class Login():
    def __init__(self, driver):
        self.driver = driver

    def input_username(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    
    def input_password(self):
        self.driver.find_element(By.ID, 'password').send_keys('standard_user')
    
    def click_button(self):
        self.driver.find_element(By.ID, 'login-button').click()
        