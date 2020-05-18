from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from .common.Alert import Alert


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.alert = Alert(self.driver)

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        self.__element(selector, index).click()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index, link_text)))

    def _get_element_text(self, selector, index):
        return self.__element(selector, index).text

    def _get_attribute(self, selector, index, attribute):
        return self.__element(selector, index).get_attribute(attribute)

    def _wait_for_presence(self, selector, wait=100):
        return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector['css'])))

    def _wait_alert(self, wait=100):
        return WebDriverWait(self.driver, wait).until(EC.alert_is_present())
