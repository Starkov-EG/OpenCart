from ..elements import WaitElem
from ..locators import AdminPage


def test_add_product(wait_time, login_to_admin):
    test_browser = login_to_admin
    wait_elem = WaitElem(test_browser, wait_time)
    catalog = test_browser.find_element_by_css_selector(AdminPage.CATALOG)
    catalog.click()
    products = wait_elem.wait_click(AdminPage.PRODUCTS)
    products.click()
    edit = test_browser.find_element_by_css_selector(AdminPage.EDIT_FIRST)
    edit.click()
    tab_data = test_browser.find_element_by_css_selector(AdminPage.TAB_DATA)
    tab_data.click()
    quantity = test_browser.find_element_by_css_selector(AdminPage.QTY)
    new_quantity = str(int(quantity.get_attribute('value'))+1)
    quantity.clear()
    quantity.send_keys(new_quantity)
    save = test_browser.find_element_by_css_selector(AdminPage.SAVE)
    save.click()
    wait_elem(AdminPage.SUCCESS)

