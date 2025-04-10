import pytest
from pages.login import Login
from data.login_data import DataLogin
from pages.product import Product
from pages.cart import Cart
from pages.checkout_1 import Checkout1
from pages.checkout_2 import Checkout2
from pages.checkout_3 import Checkout3

def test_login(setup):
    login = Login(setup)
    product = Product(setup)
    cart = Cart(setup)
    checkout1 = Checkout1(setup)
    checkout2 = Checkout2(setup)
    checkout3 = Checkout3(setup)


    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()

    title = product.check_title()
    assert title == 'Products'
    assert setup.current_url == 'https://www.saucedemo.com/inventory.html'

    product.click_add_to_chart_button()
    product.click_shopping_cart_button()
    
    name = cart.check_item_name()
    assert name == 'Sauce Labs Bike Light'

    cart.click_checkout_button()

    #Checkout 1
    checkout1.input_firstname('John')
    checkout1.input_lastname('Doe')
    checkout1.input_postalcode('12345')
    checkout1.click_checkout_button()

    #Checkout 2
    checkout2.click_finish_button()

    #Checkout 3
    assert checkout3.check_message() == 'Thank you for your order!'
    checkout3.click_finish_button()

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
