import faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from base.base_class import Base
from utilities.logger import Logger


class ClientInfoPage(Base):

    fake = Faker()

    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    first_name = "//input[@name='firstName']"
    last_name = "//input[@name='lastName']"
    postal_code = "//input[@name='postalCode']"
    continue_btn = "//input[@id='continue']"

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))
    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))


    # Actions
    def input_first_name(self,first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self,last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self,postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_continue(self):
        self.get_continue_btn().click()
        print("Click Continue")


    # Methods
    def input_information(self):
        Logger.add_start_step(method="input_information")
        self.get_current_url()
        self.input_first_name(self.fake.first_name())
        self.input_last_name(self.fake.last_name())
        self.input_postal_code("zz14o22f")
        self.click_continue()
        Logger.add_end_step(url=self.driver.current_url, method="input_information")
