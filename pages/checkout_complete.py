from selenium.webdriver.common.by import By
from locators.checkout_complete import Locators

class Checkout_complete():
    def __init__(self, driver):
        self.driver = driver

    def check_message(self):
        return self.driver.find_element(By.XPATH, Locators.message).text
    
    def click_finish_button(self):
        self.driver.find_element(By.NAME, Locators.button_back_home).click()