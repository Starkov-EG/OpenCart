from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By


class WaitElem:
    def __init__(self, driver, wait_time):
        self.driver = driver
        self.wait_time = wait_time
        self.__wd_wait = WebDriverWait(driver, wait_time)
        self.locator = ""

    def __call__(self, locator):
        self.locator = locator
        try:
            element = self.__wd_wait.\
                    until(ES.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
        except NoSuchElementException as ex:
            print(ex.msg())
        return element

    def wait_click(self, locator):
        self.locator = locator
        try:
            element = self.__wd_wait. \
                    until(ES.element_to_be_clickable((By.CSS_SELECTOR, self.locator)))
        except Exception as ex:
            print(ex.msg())
        return element
