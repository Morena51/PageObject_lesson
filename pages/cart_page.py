from .locators import CardPageLocators
from .base_page import BasePage

class CartPage(BasePage):
    def check_text_empty_basket(self):
        basket_text=self.browser.find_element(*CardPageLocators.BASKET_EMPTY_TEXT)
        assert "Your basket is empty" in basket_text.text
    
    def check_empty_basket(self):
        assert self.is_not_element_present(*CardPageLocators.BASKET_ITEMS),"BASKET_ITEMS is presented, but should not be"