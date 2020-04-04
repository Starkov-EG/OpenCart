import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://192.168.25.7/opencart", help="OpenCart URL")
    parser.addoption("--wait", action="store", default="10", help="Set elements wait time")
    parser.addoption("--pwd", action="store", default="admin", help="admin password")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def password(request):
    return request.config.getoption("--pwd")


@pytest.fixture
def browser(request, url):
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser == "ie":
        options = webdriver.IeOptions()
        driver = webdriver.Ie(options=options)
    else:
        raise Exception(f"{browser} is not supported!")
    driver.maximize_window()
    driver.implicitly_wait(wait)
    driver.get(url=url)
    request.addfinalizer(driver.close)
    return driver
