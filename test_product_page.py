import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
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