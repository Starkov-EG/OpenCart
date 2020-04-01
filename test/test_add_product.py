from ..elements import WaitElem
from ..locators import AdminPage


def test_add_product(wait_time, login_to_admin):
    new_product_name = "1-SuperPhone"
    tag = "phone"
    model = "A999"
    test_browser = login_to_admin
    wait_elem = WaitElem(test_browser, wait_time)
    catalog = test_browser.find_element_by_css_selector(AdminPage.CATALOG)
    catalog.click()
    products = test_browser.find_element_by_css_selector(AdminPage.PRODUCTS)
    products.click()
    add_new = test_browser.find_element_by_css_selector(AdminPage.ADD_NEW)
    add_new.click()
    product_name = test_browser.find_element_by_css_selector(AdminPage.PRODUCT_NAME)
    product_name.send_keys(new_product_name)
    tag_title = test_browser.find_element_by_css_selector(AdminPage.TAG_TITLE)
    tag_title.send_keys(tag)
    tab_data = test_browser.find_element_by_css_selector(AdminPage.TAB_DATA)
    tab_data.click()
    model_input = test_browser.find_element_by_css_selector(AdminPage.MODEL)
    model_input.send_keys(model)
    save = test_browser.find_element_by_css_selector(AdminPage.SAVE)
    save.click()
    wait_elem(AdminPage.SUCCESS)
