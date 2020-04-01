from .open_cart import OpenCart


class LoginAdminPage:
    URL = OpenCart.URL + "admin/"
    FA_LOCK = "h1[class = 'panel-title'] > i[class = 'fa fa-lock']"
    FA_USER = "i[class='fa fa-user']"
    USER = "input[name='username']"
    PWD = "input[name='password']"
    LOGIN = "button[type='submit']"

