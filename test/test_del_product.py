from ..elements import WaitElem
from ..locators import AdminPage


def test_add_product(wait_time, login_to_admin):
    test_browser = login_to_admin
    wait_elem = WaitElem(test_browser, wait_time)
    catalog = test_browser.find_element_by_css_selector(AdminPage.CATALOG)
    catalog.click()
    products = wait_elem.wait_click(AdminPage.PRODUCTS)
    products.click()
    check = test_browser.find_element_by_css_selector(AdminPage.CHECKBOX_FIRST)
    check.click()
    delete = test_browser.find_element_by_css_selector(AdminPage.DEL)
    delete.click()
    alert = test_browser.switch_to.alert
    alert.accept()
    wait_elem(AdminPage.SUCCESS)
