import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    select_product = '//button[@class="btn-main"]'
    cart = '//*[@id="basketContent"]/div[3]/a'

    """Getters"""

    def get_select_product(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.select_product)))
    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart)))

    """Actions"""

    def click_select_product(self):
        self.get_select_product().click()
        print('Выбрали продукт')
    def click_cart(self):
        self.get_cart().click()
        print('В корзину')

    """Methods"""

    def add_in_cart(self):
        self.get_current_url()
        self.click_select_product()
        self.click_cart()
