from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    checkout_btn = "//button[@id='checkout']"

    # Getters
    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_btn)))



    # Actions
    def click_checkout(self):
        self.get_checkout().click()
        print("Click checkout")


    # Methods
    def product_confirmation(self):
        Logger.add_start_step(method="product_confirmation")
        self.get_current_url()
        self.click_checkout()
        Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")
