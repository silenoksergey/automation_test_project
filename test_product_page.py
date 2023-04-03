from .pages.basket_page import BasketPage
from .pages.product_page import Product_Page
from .pages.login_page import LoginPage
import pytest, time

class TestProductPage():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = Product_Page(browser, url)
        page.open()
        page.should_be_product_name()
        page.should_be_add_to_cart()
        page.product_name()
        page.product_price()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.product_name_check()
        page.product_price_check()
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, url):
        page = Product_Page(browser, url)
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message()
    def test_guest_cant_see_success_message(self, browser, url):
        page = Product_Page(browser, url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, url):
        page = Product_Page(browser, url)
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message_is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = Product_Page(browser, url)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = Product_Page(browser, url)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, url)
        page.open()
        page.go_to_basket()
        page.basket_contents_is_empty()
        page.basket_empty_text()


@pytest.mark.login
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "sdlfsadk@932"
        url = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, url)
        page.open()
        browser.implicitly_wait(30)
        page.go_to_login_page()
        page.register_new_user(email, password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = Product_Page(browser, url)
        page.open()
        page.should_be_product_name()
        page.should_be_add_to_cart()
        page.product_name()
        page.product_price()
        page.add_to_cart()
        page.product_name_check()
        page.product_price_check()
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = Product_Page(browser, url)
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message()
