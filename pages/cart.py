from selenium.webdriver.common.by import By
from locators.cart import Locators

class Cart():
    def __init__(self, driver):
        self.driver = driver

    def check_item_name(self):
        name = self.driver.find_element(By.XPATH, Locators.item_name).text
        return name

    def click_checkout_button(self):
        self.driver.find_element(By.NAME, Locators.button_checkout).click()
    
    def check_title(self):
        return self.driver.find_element(By.XPATH, Locators.title).text