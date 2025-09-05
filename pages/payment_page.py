from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    finish_btn = "//button[@id='finish']"

    # Getters
    def get_finish_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_btn)))


    # Actions
    def click_finish(self):
        self.get_finish_btn().click()
        print("Click finish")

    # Methods
    def payment(self):
        Logger.add_start_step(method="payment")
        self.get_current_url()
        self.click_finish()
        Logger.add_end_step(url=self.driver.current_url, method="payment")
