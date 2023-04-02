

from .pages.product_page import Product_Page

def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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

