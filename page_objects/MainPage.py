from .BasePage import BasePage
from .ProductPage import ProductPage


class MainPage(BasePage):
    """Главная страница"""
    IT = {'css': '#content > div.row'}
    PRODUCTS = {'css': IT['css'] + ' .product-layout'}
    PRODUCT_NAMES = {'css': PRODUCTS['css'] + ' .caption h4 a'}


    def click_featured_product(self, number):
        index = number - 1
        self._click(self.PRODUCTS, index=index)
        return ProductPage(self.driver)

    def get_featured_product_name(self, number):
        index = number - 1
        return self._get_element_text(self.PRODUCT_NAMES, index=index)
