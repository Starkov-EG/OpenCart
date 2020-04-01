import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from .locators.login_admin_page import LoginAdminPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Web Browser")
    parser.addoption("--wait", action="store", default="60", help="Set wait")
    parser.addoption("--pwd", action="store", help="admin password", required=True)


@pytest.fixture
def test_browser(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        options = Options()
        options.headless = True
        web_drv = webdriver.Firefox(options=options)
    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        #options.add_argument("headless")
        web_drv = webdriver.Chrome(options=options)
    elif browser == "ie":
        options = webdriver.IeOptions()
    else:
        raise Exception(f"Browser {browser} is not supported!")
    web_drv.maximize_window()
    yield web_drv
    web_drv.quit()


@pytest.fixture
def wait_time(request):
    wait = request.config.getoption("--wait")
    return int(wait)


@pytest.fixture()
def login_to_admin(test_browser, request):
    test_browser.get(LoginAdminPage.URL)
    user = "admin"
    password = request.config.getoption("--pwd")
    user_input = test_browser.find_element_by_css_selector(LoginAdminPage.USER)
    user_input.send_keys(user)
    password_input = test_browser.find_element_by_css_selector(LoginAdminPage.PWD)
    password_input.send_keys(password)
    login_btn = test_browser.find_element_by_css_selector(LoginAdminPage.LOGIN)
    login_btn.click()
    return test_browser
