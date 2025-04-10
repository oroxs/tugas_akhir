import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    #precondition
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://saucedemo.com')

    yield driver
    #Post condition
    driver.close()