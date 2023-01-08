from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Electronics_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    laptops = '//*[@id="app"]/div[2]/div/div[3]/div[1]/div/div/ul[2]/li[7]/a'

    """Getters"""

    def get_laptops(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.laptops)))

    """Actions"""

    def click_laptops(self):
        self.get_laptops().click()
        print('Выбрали раздел ноутбуками')

    """Methods"""

    def select_laptops(self):
        self.get_current_url()
        self.click_laptops()
