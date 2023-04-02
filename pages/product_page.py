from .base_page import BasePage
from .locators import ProductPageLocators
class Product_Page(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
    def product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name
    def product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price
    def product_name_check(self):
        assert self.product_name() == self.product_name_in_allert(), "The name of the product in the cart does not match"
    def product_price_check(self):
        assert self.product_price() == self.product_price_in_allert(), "The price of the product in the cart does not match"
    def product_price_in_allert(self):
        product_price_in_allert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CHECK).text
        return product_price_in_allert
    def product_name_in_allert(self):
        product_name_in_allert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CHECK).text
        return product_name_in_allert
    def should_be_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "add to cart link is not presented"
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name link is not presented"
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "product price link is not presented"

