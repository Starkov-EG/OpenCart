from ..locators import ProductPage
from ..elements import WaitElem


def test_wait_fb_like(test_browser, wait_time):
    wait_elem = WaitElem(test_browser, wait_time)
    test_browser.get(ProductPage.URL)
    wait_elem(ProductPage.FB_FRAME)


def test_to_cart(test_browser, wait_time):
    wait_elem = WaitElem(test_browser, wait_time)
    test_browser.get(ProductPage.URL)
    elem_to_cart = test_browser.find_element_by_css_selector(ProductPage.TO_CART)
    elem_to_cart.click()
    wait_elem(ProductPage.ALERT_SUCCESS)


def test_3(test_browser, wait_time):
    wait_elem = WaitElem(test_browser, wait_time)
    test_browser.get(ProductPage.URL)
    wait_elem(ProductPage.BRAND)


def test_4(test_browser, wait_time):
    wait_elem = WaitElem(test_browser, wait_time)
    test_browser.get(ProductPage.URL)
    wait_elem(ProductPage.IMAGE)


def test_5(test_browser, wait_time):
    wait_elem = WaitElem(test_browser, wait_time)
    test_browser.get(ProductPage.URL)
    wait_elem(ProductPage.PRICE)
