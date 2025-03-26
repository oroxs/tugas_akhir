from selenium.webdriver.common.by import By
from locators.product import Locators

class Product():
    def __init__(self, driver):
        self.driver = driver

    def check_title(self):
        title = self.driver.find_element(By.XPATH, Locators.title).text
        return title
    
    def click_add_to_chart_button(self):
        self.driver.find_element(By.NAME, Locators.button_add_to_cart).click()
    
    def click_shopping_cart_button(self):
        self.driver.find_element(By.XPATH, Locators.button_shopping_cart).click()