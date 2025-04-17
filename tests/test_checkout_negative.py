import pytest
from data.checkout_data import DataUser
from data.login_data import DataLogin
from pages.login import Login
from pages.product import Product
from pages.cart import Cart
from pages.checkout import Checkout

checkout = DataUser.negative_users
users = DataLogin.valid_user
         
def do_checkout(setup, username, password, first, last, zip_code):
    login = Login(setup)
    product = Product(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)

    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    assert product.check_title() == 'Products'
    assert setup.current_url == 'https://www.saucedemo.com/inventory.html'

    product.click_add_to_chart_button()
    product.click_shopping_cart_button()
    assert cart.check_item_name() == 'Sauce Labs Bike Light'
    cart.click_checkout_button()

    checkout.input_firstname(first)
    checkout.input_lastname(last)
    checkout.input_postalcode(zip_code)
    checkout.click_checkout_button()

    return checkout


@pytest.mark.parametrize('username, password', users)
@pytest.mark.parametrize('first, last, zip_code, expected_error',checkout )
def test_checkout_negative_cases(setup, username, password, first, last, zip_code, expected_error):
    checkout = do_checkout(setup, username, password, first, last, zip_code)
    assert checkout.check_error_message() == expected_error
    assert setup.current_url == 'https://www.saucedemo.com/checkout-step-one.html'