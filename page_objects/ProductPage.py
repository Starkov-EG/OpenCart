from .BasePage import BasePage
import logging


class ProductPage(BasePage):
    """Страница продукта"""

    ADD_TO_WISHLIST = {'css': '[data-original-title="Add to Wish List"]'}
    ADD_TO_CART = {'css': '#button-cart'}

    def __init__(self, browser):
        super().__init__(browser)
        logger = logging.getLogger("ProductPage")
        logger.info("Инициализация страницы")

    def add_to_wishlist(self):
        self._click(self.ADD_TO_WISHLIST)
        return self

    def add_to_cart(self):
        self._click(self.ADD_TO_CART)
        return self
