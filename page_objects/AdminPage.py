from .BasePage import BasePage



class AdminPage(BasePage):
    """ Страница администратора """

    FA_LOCK = {"css": "h1[class = 'panel-title'] > i[class = 'fa fa-lock']"}
    FA_USER = {"css": "i[class='fa fa-user']"}
    USER_INPUT = {"css": "input[name='username']"}
    PASSWORD_INPUT = {"css": "input[name='password']"}
    LOGIN_BUTTON = {"css": "button[type='submit']"}

    CATALOG = {"css": "#menu-catalog > a"}
    PRODUCTS = {"css": "#collapse1 > li:nth-child(2) > a"}
    ADD_NEW = {"css": "#content > div.page-header > div > div > a"}
    PRODUCT_NAME = {"css": "#input-name1"}
    TAG_TITLE = {"css": "#input-meta-title1"}
    SAVE = {"css": "#content > div.page-header > div > div > button"}
    TAB_DATA = {"css": "#form-product > ul > li:nth-child(2) > a"}
    MODEL = {"css": "#input-model"}
    SUCCESS = {"css": "#content > div.container-fluid > div.alert.alert-success.alert-dismissible"}
    EDIT_FIRST = {"css": "#form-product > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > a"}
    QTY = {"css": "#input-quantity"}
    CHECKBOX_FIRST = {"css": "#form-product > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]"}
    DEL = {"css": "#content > div.page-header > div > div > button.btn.btn-danger"}

    def login_admin(self, user, password):
        self._input(self.USER_INPUT, user)
        self._input(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)
        return self

    def click_products(self):
        self._click(self.CATALOG)
        self._wait_for_visible(self.PRODUCTS)
        self._click(self.PRODUCTS)
        return self

    def add_new_product(self, new_product):
        self._click(self.ADD_NEW)
        self._input(self.PRODUCT_NAME, new_product["name"])
        self._input(self.TAG_TITLE, new_product["tag"])
        self._click(self.TAB_DATA)
        self._input(self.MODEL, new_product["model"])
        self._click(self.SAVE)
        return self

    def operation_success_wait(self):
        self._wait_for_visible(self.SUCCESS)
        return self

    def edit_product_quantity(self, add_quantity):
        self._click(self.EDIT_FIRST)
        self._click(self.TAB_DATA)
        quantity = self._get_attribute(AdminPage.QTY, 0, "value")
        new_quantity = str(int(quantity) + add_quantity)
        self._input(self.QTY, new_quantity)
        self._click(self.SAVE)
        return self

    def del_product(self):
        self._click(self.CHECKBOX_FIRST)
        self._click(self.DEL)
        self.driver.switch_to.alert\
            .accept()
        return self
