from .BasePage import BasePage


class CartPage(BasePage):
    """Экран корзины"""

    BUTTONS = {'css': '.buttons'}
    CHECKOUT_BUTTON = {'css': BUTTONS['css'] + ' a.btn-primary'}

    def checkout(self):
        self._click(self.CHECKOUT_BUTTON)

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self
