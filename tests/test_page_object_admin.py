# pytest tests\test_page_object_admin.py --url="http://192.168.25.7/opencart/admin" --pwd="admin" -s -v
from ..page_objects import AdminPage
import logging
import time

new_product = {"name": "1-SuperPhone", "tag": "phone", "model": "A999", "image": "superphone.jpg"}
GET_COUNT_PRODUCTS = "SELECT COUNT(1) FROM oc_product"
GET_PRODUCT_QTY = "SELECT quantity FROM oc_product WHERE model = '" + new_product['model'] + \
                  "' ORDER BY date_added LIMIT 1"


def test_add_product(browser, password, sql_cursor):
    sql_cursor.execute(GET_COUNT_PRODUCTS)
    count_products_before = sql_cursor.fetchall()[0][0]
    AdminPage(browser)\
        .login_admin(user="admin", password=password)\
        .click_products()\
        .add_new_product(new_product)\
        .operation_success_wait()
    time.sleep(5)
    sql_cursor.execute(GET_COUNT_PRODUCTS)
    count_products_after = sql_cursor.fetchall()[0][0]
    assert int(count_products_after) == int(count_products_before) + 1


def test_edit_product(browser, password, sql_cursor):
    sql_cursor.execute(GET_PRODUCT_QTY)
    product_qty_before = sql_cursor.fetchall()[0][0]
    add_product_qty = 9
    AdminPage(browser).\
        login_admin(user="admin", password=password)\
        .click_products()\
        .edit_product_quantity(add_product_qty)\
        .operation_success_wait()
    sql_cursor.execute(GET_COUNT_PRODUCTS)
    product_qty_after = sql_cursor.fetchall()[0][0]
    assert int(product_qty_after) == int(product_qty_before) + add_product_qty



def test_del_product(browser, password, sql_cursor):
    sql_cursor.execute(GET_COUNT_PRODUCTS)
    count_products_before = sql_cursor.fetchall()[0][0]
    AdminPage(browser).\
        login_admin(user="admin", password=password)\
        .click_products().del_product()\
        .operation_success_wait()
    sql_cursor.execute(GET_COUNT_PRODUCTS)
    count_products_after = sql_cursor.fetchall()[0][0]
    assert int(count_products_after) == int(count_products_before) - 1
