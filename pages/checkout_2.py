from selenium.webdriver.common.by import By
from locators.checkout2 import Locators

class Checkout2():
    def __init__(self, driver):
        self.driver = driver

    def click_finish_button(self):
        self.driver.find_element(By.NAME, Locators.button_finish).click()