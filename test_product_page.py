from .pages.product_page import ProductPage

def test_guest_can_add_product_to_cart(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser.get(link)
    product_page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code() 
    product_page.check_add_product_message() #проверяем название продукта в сообщении
    product_page.check_add_product_price() # проверяем стоимость товаров в корзине