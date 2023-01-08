import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Laptops_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    catalog = '//*[@id="catalog"]/div[5]/div[2]/div/ul/li/ul/li[1]/a'
    brand = '//*[@id="filters"]/div[2]/div[2]/fieldset/label[2]'
    diagonal = '//*[@id="filters"]/div[7]/div[2]/fieldset/label[4]'
    cpu_type = '//*[@id="filters"]/div[12]/div[2]/fieldset/label[1]'
    cart = '//*[@id="basketContent"]/div[3]/a'
    product = '//*[@id="c137867758"]/div/a/div[1]/div[2]/img'

    """Getters"""

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.catalog)))
    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.brand)))
    def get_diagonal(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.diagonal)))
    def get_cpu_type(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cpu_type)))
    def get_select_laptop(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//button[@class="btn-main"]')))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart)))
    def get_product(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.product)))
    def get_closed_product(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/a')))

    """Actions"""

    def click_catalog(self):
        self.get_catalog().click()
        print('Выбрали раздел каталога (ноутбуки)')
    def click_brand(self):
        self.get_brand().click()
        print('Выбрали бранд')
    def click_diagonal(self):
        self.get_diagonal().click()
        print('Выбрали диагональ')
    def click_cpu_type(self):
        self.get_cpu_type().click()
        print('Выбрали ЦПУ')
    def click_select_laptop(self):
        self.get_select_laptop().click()
        print('Выбрали ноутбук')
    def click_cart(self):
        self.get_cart().click()
        print('В корзину')
    def click_product(self):
        self.get_product().click()
    def closed_product(self):
        self.get_closed_product().click()

    """Methods"""

    def select_laptop(self):
        self.get_current_url()
        time.sleep(1)
        self.click_catalog()
        time.sleep(1)
        self.click_brand()
        time.sleep(1)
        self.click_diagonal()
        time.sleep(1)
        self.click_cpu_type()
        time.sleep(1)
        self.click_product()
        time.sleep(1)
        self.click_select_laptop()
        time.sleep(1)
        self.closed_product()
        self.click_cart()
