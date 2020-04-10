# pytest tests\test_page_object_admin.py --url="http://192.168.25.7/opencart/admin" --pwd="admin" -s -v
from ..page_objects import AdminPage
import logging
import time


def test_add_product(browser, password):
    new_product = {"name": "1-SuperPhone", "tag": "phone", "model": "A999", "image": "superphone.jpg"}
    AdminPage(browser)\
        .login_admin(user="admin", password=password)\
        .click_products()\
        .add_new_product(new_product)\
        .operation_success_wait()
    time.sleep(5)


def test_edit_product(browser, password):
    add_product_qty = 9
    AdminPage(browser).\
        login_admin(user="admin", password=password)\
        .click_products()\
        .edit_product_quantity(add_product_qty)\
        .operation_success_wait()


def test_del_product(browser, password):
    AdminPage(browser).\
        login_admin(user="admin", password=password)\
        .click_products().del_product()\
        .operation_success_wait()
