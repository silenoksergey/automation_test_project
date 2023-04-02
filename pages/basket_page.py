from .locators import Basket_page
from .base_page import BasePage

class BasketPage(BasePage):
    def basket_contents_is_empty(self):
        assert self.is_not_element_present(*Basket_page.BASKET_ITEMS), \
            "the basket is full and should be empty"
    def basket_empty_text(self):
        self.is_element_present(*Basket_page.BASKET_CONTENTS_IS_EMPTY)
