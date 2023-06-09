from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.SUBSTRING_LOGIN in self.browser.current_url, "URL does not contain a 'login' substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()
        self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS)



