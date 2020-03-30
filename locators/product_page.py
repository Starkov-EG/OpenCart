class ProductPage:
    URL = "https://demo.opencart.com/index.php?route=product/product&product_id=40"
    TO_WISH_LIST = "#content > " \
                   "div:nth-child(1) > div.col-sm-4 > div.btn-group > button:nth-child(1) > i"
    FB_FRAME = "iframe[data-testid = 'fb:like Facebook Social Plugin']"
    TO_CART = "#button-cart"
    ALERT_SUCCESS = "#product-product > div.alert.alert-success.alert-dismissible"
    BRAND = "#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(3) > li:nth-child(1) > a"
    PRICE = "#content > div:nth-child(1) > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2"
    IMAGE = "#content > div:nth-child(1) > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a > img"
    QTY = "#input-quantity"
