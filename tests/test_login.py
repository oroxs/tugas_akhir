import pytest
from pages.login import Login
from data.login_data import DataLogin
from pages.product import Product

def test_login(setup):
    login = Login(setup)
    product = Product(setup)

    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()

    title = product.check_title()
    assert title == 'Products'
    assert setup.current_url == 'https://www.saucedemo.com/inventory.html'

users = DataLogin.users
         
@pytest.mark.parametrize('username, password, error',users)
def test_invalid_login(setup, username, password, error):
    login = Login(setup)
    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    # Check error message
    error_message = login.check_error_message()

    assert error_message == error
    assert setup.current_url == 'https://www.saucedemo.com/'