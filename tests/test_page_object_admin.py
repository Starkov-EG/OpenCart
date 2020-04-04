from ..page_objects import AdminPage


def test_add_product(browser, password):
    new_product = {"name": "1-SuperPhone", "tag": "phone", "model": "A999"}
    AdminPage(browser)\
        .login_admin(user="admin", password=password)\
        .click_products()\
        .add_new_product(new_product)\
        .operation_success_wait()


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
