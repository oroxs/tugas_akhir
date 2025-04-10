from selenium.webdriver.common.by import By
from locators.login import Locators

class Login():
    def __init__(self, driver):
        self.driver = driver

    def input_username(self,username):
        self.driver.find_element(By.ID, Locators.input_username).send_keys(username)
    
    def input_password(self,password):
        self.driver.find_element(By.ID, Locators.input_password).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(By.ID, Locators.login_button).click()
    
    def check_error_message(self):
        return self.driver.find_element(By.XPATH, Locators.error_message).text
        