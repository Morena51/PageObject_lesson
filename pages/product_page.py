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
