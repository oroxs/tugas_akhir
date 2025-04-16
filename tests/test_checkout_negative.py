import pytest
from data.checkout_data import DataUser
from data.login_data import DataLogin
from pages.login import Login
from pages.product import Product
from pages.cart import Cart
from pages.checkout import Checkout

checkout = DataUser.negative_users
users = DataLogin.valid_user
         
@pytest.mark.parametrize('username, password',users)

def test_checkout_without_any_input(setup,username,password):
    login = Login(setup)
    product = Product(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)

    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    title = product.check_title()
    assert title == 'Products'
    assert setup.current_url == 'https://www.saucedemo.com/inventory.html'

    #add to cart
    product.click_add_to_chart_button()
    product.click_shopping_cart_button()
    name = cart.check_item_name()
    assert name == 'Sauce Labs Bike Light'

    cart.click_checkout_button()

    #Checkout 
    checkout.input_firstname("")
    checkout.input_lastname("Doe")
    checkout.input_postalcode("321222")
    checkout.click_checkout_button()
    assert checkout.check_error_message() == 'Error: First Name is required' 
    assert setup.current_url == 'https://www.saucedemo.com/checkout-step-one.html'

@pytest.mark.parametrize('username, password',users)
def test_checkout_without_lastname(setup,username,password):
    login = Login(setup)
    product = Product(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)

    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    title = product.check_title()
    assert title == 'Products'
    assert setup.current_url == 'https://www.saucedemo.com/inventory.html'

    #add to cart
    product.click_add_to_chart_button()
    product.click_shopping_cart_button()
    name = cart.check_item_name()
    assert name == 'Sauce Labs Bike Light'

    cart.click_checkout_button()

    #Checkout 
    checkout.input_firstname("Jone")
    checkout.input_lastname("")
    checkout.input_postalcode("321222")
    checkout.click_checkout_button()
    assert checkout.check_error_message() == 'Error: Last Name is required' 
    assert setup.current_url == 'https://www.saucedemo.com/checkout-step-one.html'


@pytest.mark.parametrize('username, password',users)
def test_checkout_without_postalcode(setup,username,password):
    login = Login(setup)
    product = Product(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)

    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    title = product.check_title()
    assert title == 'Products'
    assert setup.current_url == 'https://www.saucedemo.com/inventory.html'

    #add to cart
    product.click_add_to_chart_button()
    product.click_shopping_cart_button()
    name = cart.check_item_name()
    assert name == 'Sauce Labs Bike Light'

    cart.click_checkout_button()

    #Checkout 
    checkout.input_firstname("Jone")
    checkout.input_lastname("Doe")
    checkout.input_postalcode("")
    checkout.click_checkout_button()
    assert checkout.check_error_message() == 'Error: Postal Code is required' 
    assert setup.current_url == 'https://www.saucedemo.com/checkout-step-one.html'