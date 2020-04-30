import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import mysql.connector as mariadb


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://192.168.25.7/opencart", help="OpenCart URL")
    parser.addoption("--wait", action="store", default="10", help="Set elements wait time")
    parser.addoption("--pwd", action="store", default="admin", help="admin password")


logger = logging.getLogger("conftest")


@pytest.fixture(autouse="True")
def log(caplog):
    caplog.set_level("INFO")


class MyListener(AbstractEventListener):

    logger = logging.getLogger("browser")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"I'm navigating to {url}")
        print("****************************")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"I'm on {url}")

    def before_navigate_back(self, driver):
        self.logger.info(f"I'm navigating back")

    def after_navigate_back(self, driver):
        self.logger.info(f"I'm back!")

    def before_find(self, by, value, driver):
        self.logger.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        self.logger.info(f"I've found '{value}' with '{by}'")

    def before_click(self, element, driver):
        self.logger.info(f"I'm clicking {element}")

    def after_click(self, element, driver):
        self.logger.info(f"I've clicked {element}")

    def before_execute_script(self, script, driver):
        self.logger.info(f"I'm executing '{script}'")

    def after_execute_script(self, script, driver):
        self.logger.info(f"I've executed '{script}'")

    def before_quit(self, driver):
        self.logger.info(f"I'm getting ready to terminate {driver}")

    def after_quit(self, driver):
        self.logger.info(f"WASTED!!!")

    def on_exception(self, exception, driver):
        self.logger.error(f'Oooops i got: {exception}')
        driver.save_screenshot(f'exception_{time.strftime("%Y%m%d-%H%M%S")}.png')


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def password(request):
    return request.config.getoption("--pwd")


@pytest.fixture
def browser(request, url):
    logger.info("Инициализация фикстуры браузера")
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")
    if browser == "chrome":
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = Options()
        #options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser == "ie":
        options = webdriver.IeOptions()
        driver = webdriver.Ie(options=options)
    else:
        raise Exception(f"{browser} is not supported!")
    driver.maximize_window()
    driver.implicitly_wait(wait)
    driver.get(url=url)

    def fin():
        logger.info("Завершение фикстуры браузера")
        if browser == "Chrome":
            browser_logs = driver.get_log("browser")
            for log in browser_logs:
                if log['level'] == "SEVERE":
                    logger.error(log['message'])
                    print(log['message'])
        driver.close()
    request.addfinalizer(fin)
    return EventFiringWebDriver(driver=driver, event_listener=MyListener())


@pytest.fixture()
def sql_cursor(request, url):
    MARIADB_SERVER = url.split("/")[2]
    MARIADB_DATABASE = "opencart"
    MARIADB_USER = "remote_user"
    MARIADB_PASSWORD = "PASSWORD"
    db_connection = mariadb.connect(
        user=MARIADB_USER,
        database=MARIADB_DATABASE,
        host=MARIADB_SERVER,
        password=MARIADB_PASSWORD
    )

    def fin():
        db_connection.cursor().close()
    request.addfinalizer(fin)
    return db_connection.cursor()
