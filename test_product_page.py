import pytest
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip
def test_guest_can_add_product_to_cart(browser,link):
    #link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    browser.get(link)
    product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code() 
    product_page.check_add_product_message() #проверяем название продукта в сообщении
    product_page.check_add_product_price() # проверяем стоимость товаров в корзине

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page.open()
    product_page.add_product_to_basket() # добавляем товар в корзину
    product_page.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE) #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page.open()
    product_page.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE) # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

"""def test_message_disappeared_after_adding_product_to_cart(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code() 
    product_page.is_disappeared(*ProductPageLocators.BASKET_MESSAGE) # Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
