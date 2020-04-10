from ..page_objects import MainPage, UserPage, ProductPage, CartPage
import time


def test_add_to_wish_list(browser):
    product_name = MainPage(browser).get_featured_product_name(1)
    print(product_name)
    MainPage(browser) \
        .click_featured_product(1) \
        .add_to_wishlist() \
        .alert.click_login()
    UserPage(browser) \
        .login_user(email="test@test.ru", password="test") \
        .open_wishlist() \
        .verify_product
    time.sleep(10)


def test_add_to_cart(browser, url):
    product_name = MainPage(browser).get_featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser) \
        .add_to_cart() \
        .alert.click_to_cart()
    CartPage(browser) \
        .verify_product(product_name) \
        .checkout()
    UserPage(browser) \
        .login_user(email="test@test.ru", password="test") \
        .verify_payment_form()
    time.sleep(10)

