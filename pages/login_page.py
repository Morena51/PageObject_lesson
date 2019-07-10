from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url=self.browser.current_url
        assert LoginPageLocators.url in login_url, "URL страницы логина НЕ содержит подстроку login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self,email, password):
        email_field=self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field=self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)
        password_field_repead=self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPIAD)
        password_field_repead.send_keys(password)
        btn=self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        btn.click()