import pytest
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
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

@pytest.mark.xfail  #падающий тест, требовалось проверить в одном из заданий курса (на отрицательные  проверки)
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
    
@pytest.mark.xfail #падающий тест, требовалось проверить в одном из заданий курса (на отрицательные  проверки)
def test_message_disappeared_after_adding_product_to_cart(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code() 
    product_page.is_disappeared(*ProductPageLocators.BASKET_MESSAGE) # Проверяем, что нет сообщения об успехе с помощью is_disappeared"""

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.should_be_login_link() #Проверяем что со страницы продукта можно попасть на страницу логина

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.go_to_basket_page()
    basket_page=CartPage(browser,browser.current_url)
    basket_page.check_text_empty_basket() # проверяем что есть текст для пустой корзины
    basket_page.check_empty_basket() # проверяем корзина пустая

@pytest.mark.for_user_test
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True) # фикстура для регистрации пользователя
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser=browser
        self.browser.get(link)
        login_page=LoginPage(self.browser, link)
        email = str(time.time()) + "@fakemail.org"
        password="Qwerty"+str(time.time())
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        browser.get(link)
        product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        product_page.open()
        product_page.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE) # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        browser.get(link)
        product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code() 
        product_page.check_add_product_message() #проверяем название продукта в сообщении
        product_page.check_add_product_price() # проверяем стоимость товаров в корзине