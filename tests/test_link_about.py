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
from selenium.webdriver.common.by import By


def test_link_about():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    print("Start Test")
    login = LoginPage(driver)
    login.authorization_user()
    mp = MainPage(driver)
    mp.select_menu_about()
    print("Test Success!")
    driver.quit()


