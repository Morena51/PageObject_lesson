from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket=self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()

    def check_add_product_message(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_message=self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE)
        assert product_name.text==product_name_message.text

    def check_add_product_price(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_message=self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text==product_price_message.text

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True