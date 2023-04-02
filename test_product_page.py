import time

import pytest
from .pages.product_page import Product_Page
# @pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",])
class TestProductPage():
    # def test_guest_can_add_product_to_basket(self, browser, url):
    #     page = Product_Page(browser, url)
    #     page.open()
    #     page.should_be_product_name()
    #     page.should_be_add_to_cart()
    #     page.product_name()
    #     page.product_price()
    #     page.add_to_cart()
    #     page.solve_quiz_and_get_code()
    #     page.product_name_check()
    #     page.product_price_check()
    # @pytest.mark.xfail
    # def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, url):
    #     page = Product_Page(browser, url)
    #     page.open()
    #     page.add_to_cart()
    #     page.should_not_be_success_message()
    # def test_guest_cant_see_success_message(self, browser, url):
    #     page = Product_Page(browser, url)
    #     page.open()
    #     page.should_not_be_success_message()
    #
    # @pytest.mark.xfail
    # def test_message_disappeared_after_adding_product_to_basket(self, browser, url):
    #     page = Product_Page(browser, url)
    #     page.open()
    #     page.add_to_cart()
    #     page.should_not_be_success_message_is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = Product_Page(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = Product_Page(browser, url)
        page.open()
        page.go_to_login_page()