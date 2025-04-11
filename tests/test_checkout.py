import pytest
from data.checkout_data import DataUser
from data.login_data import DataLogin
from pages.login import Login
from pages.product import Product
from pages.cart import Cart
from pages.checkout_1 import Checkout1
from pages.checkout_2 import Checkout2
from pages.checkout_3 import Checkout3

checkout = DataUser.users
users = DataLogin.valid_user
         
@pytest.mark.parametrize('firstname, lastname, postalcode',checkout)
@pytest.mark.parametrize('username, password',users)

def test_checkout(setup,firstname, lastname, postalcode,username, password):
    login = Login(setup)
    product = Product(setup)
    cart = Cart(setup)
    checkout1 = Checkout1(setup)
    checkout2 = Checkout2(setup)
    checkout3 = Checkout3(setup)


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

    cart.click_checkout_button()

    #Checkout 1
    checkout1.input_firstname(firstname)
    checkout1.input_lastname(lastname)
    checkout1.input_postalcode(postalcode)
    checkout1.click_checkout_button()

    #Checkout 2
    checkout2.click_finish_button()

    #Checkout 3
    assert checkout3.check_message() == 'Thank you for your order!'
    checkout3.click_finish_button()
