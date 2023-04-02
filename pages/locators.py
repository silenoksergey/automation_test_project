from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    SUBSTRING_LOGIN = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME_CHECK = (By.CSS_SELECTOR, "div#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong")
    PRODUCT_PRICE_CHECK = (By.CSS_SELECTOR, "div#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in > div.alertinner")