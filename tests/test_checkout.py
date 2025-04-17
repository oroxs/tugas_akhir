import pytest
from data.checkout_data import DataUser
from data.login_data import DataLogin
from pages.login import Login
from pages.product import Product
from pages.cart import Cart
from pages.checkout import Checkout
from pages.checkout_complete import Checkout_complete

checkout = DataUser.users
users = DataLogin.valid_user
         
@pytest.mark.parametrize('firstname, lastname, postalcode',checkout)
@pytest.mark.parametrize('username, password',users)

def test_checkout(setup,firstname, lastname, postalcode,username, password):
    login = Login(setup)
    product = Product(setup)
    cart = Cart(setup)
    checkout = Checkout(setup)
    complete = Checkout_complete(setup)


    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    title = product.check_title()
    assert title == 'Products'
    assert setup.current_url == 'https://www.saucedemo.com/inventory.html'
    
    product.click_add_to_chart_button()
    product.click_shopping_cart_button()
    name = cart.check_item_name()
    assert name == 'Sauce Labs Bike Light'
    
    #Chart Page 
    title = cart.check_title()
    assert title == 'Your Cart'
    cart.click_checkout_button()

    #Checkout 
    title = checkout.check_title()
    assert title == 'Checkout: Your Information'
    checkout.input_firstname(firstname)
    checkout.input_lastname(lastname)
    checkout.input_postalcode(postalcode)
    checkout.click_checkout_button()
    checkout.click_finish_checkout()

    #finsih checkout
    assert complete.check_title() == 'Checkout: Complete!'
    assert complete.check_message() == 'Thank you for your order!'
    complete.click_finish_button()
