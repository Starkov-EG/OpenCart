class Alert:
    SUCCESS_ALERT = {'css': '.alert-success'}
    SUCCESS_ALERT_LOGIN = {'css': SUCCESS_ALERT['css'] + ' > a:nth-child(2)'}
    SUCCESS_ALERT_TO_CART = {'css': SUCCESS_ALERT['css'] + ' > a:nth-child(2)'}

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        # А как нам заиспоьзовать здесь BasePage?
        self.driver.find_element_by_css_selector(self.SUCCESS_ALERT_LOGIN['css']).click()

    def click_to_cart(self):
        self.driver.find_element_by_css_selector(self.SUCCESS_ALERT_LOGIN['css']).click()
