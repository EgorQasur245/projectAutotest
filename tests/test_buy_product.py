import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.finish_page import FinishPage
from pages.payment_page import PaymentPage
from pages.client_info_page import ClientInfoPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# @pytest.mark.order(3)
def test_buy_product_1(set_group,set_up):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    print("Start Test 1")
    login = LoginPage(driver)
    login.authorization_user()
    mp = MainPage(driver)
    mp.select_product_1()
    cp = CartPage(driver)
    cp.product_confirmation()
    cip = ClientInfoPage(driver)
    cip.input_information()
    p = PaymentPage(driver)
    p.payment()
    f = FinishPage(driver)
    f.finish()
    print("Test Success! 1")
    driver.quit()

# @pytest.mark.order(1)
def test_buy_product_2(set_up):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    print("Start Test 2")
    login = LoginPage(driver)
    login.authorization_user()
    mp = MainPage(driver)
    mp.select_product_2()
    cp = CartPage(driver)
    cp.product_confirmation()
    print("Test Success! 2")
    driver.quit()

# @pytest.mark.order(2)
def test_buy_product_3(set_up):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    print("Start Test 3")
    login = LoginPage(driver)
    login.authorization_user()
    mp = MainPage(driver)
    mp.select_product_3()
    cp = CartPage(driver)
    cp.product_confirmation()
    print("Test Success! 3")
    driver.quit()


