from selenium.webdriver.common.by import By
from locators.checkout import Locators

class Checkout():
    def __init__(self, driver):
        self.driver = driver

    def input_firstname(self,firstname):
        self.driver.find_element(By.NAME, Locators.input_firstname).send_keys(firstname)
    
    def input_lastname(self,lastname):
        self.driver.find_element(By.NAME, Locators.input_lastname).send_keys(lastname)
    
    def input_postalcode(self,postalcode):
        self.driver.find_element(By.NAME, Locators.input_postalcode).send_keys(postalcode)

    def click_checkout_button(self):
        self.driver.find_element(By.NAME, Locators.checkout_button).click()
    
    def click_finish_checkout(self):
        self.driver.find_element(By.NAME, Locators.button_finish).click()