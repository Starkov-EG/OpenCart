import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Web Browser")
    parser.addoption("--wait", action="store", default="60", help="Set wait")


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
