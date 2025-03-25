from selenium.webdriver.common.by import By

class Product():
    def __init__(self, driver):
        self.driver = driver

    def check_title(self):
        title = self.driver.find_element(By.XPATH, '//span[@data-test="title"]').text
        return title