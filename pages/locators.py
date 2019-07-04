from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form")
    LOGIN_EMAIL=(By.CSS_SELECTOR,"input[name=login-username]")
    LOGIN_PASSWORD=(By.CSS_SELECTOR,"input[name=login-password]")
    BUTTON_LOGIN=(By.CSS_SELECTOR,"button[name='login_submit']")
    REGISTRATION_FORM=(By.CSS_SELECTOR,"#register_form")
    REGISTRATION_EMAIL=(By.CSS_SELECTOR,"input[name=registration-email]")
    REGISTRATION_PASSWORD=(By.CSS_SELECTOR,"input[name=registration-password1]")
    REGISTRATION_PASSWORD_REPIAD=(By.CSS_SELECTOR,"input[name=registration-password2]")
    BUTTON_REGISTRATION=(By.CSS_SELECTOR,"button[name='registration_submit']")
    url="login"
class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET=(By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_main>h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".product_main>p.price_color")
    BASKET_MESSAGE=(By.CSS_SELECTOR,".alert:nth-child(1) strong")
    BASKET_PRICE=(By.CSS_SELECTOR,".alert:nth-child(3) strong")
