from .BasePage import BasePage


class UserPage(BasePage):
    """Страница пользователя"""

    RIGHT_MENU = {'css': '#column-right'}
    WISH_LIST = {'css': RIGHT_MENU['css'] + ' a:nth-child(5)'}
    PAYMENT_FORM = {'css': '#payment-new'}
    LOGIN_EMAIL_INPUT = {'css': '#input-email'}
    LOGIN_PASSWORD_INPUT = {'css': '#input-password'}
    LOGIN_BUTTON = {'css': 'input[value=Login]'}

    def login_user(self, email, password):
        self._input(self.LOGIN_EMAIL_INPUT, email)
        self._input(self.LOGIN_PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)
        return self

    def open_wishlist(self):
        self._click(self.WISH_LIST)
        return self

    def verify_payment_form(self):
        self._wait_for_visible(self.PAYMENT_FORM)
        return self

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self
