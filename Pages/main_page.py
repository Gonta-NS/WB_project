from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    url = 'https://www.wildberries.ru/'
    electronics = '//a[@class="menu-burger__main-list-link menu-burger__main-list-link--4830"]'

    """Getters"""

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//button[@class="nav-element__burger j-menu-burger-btn j-wba-header-item hide-mobile"]')))
    def get_electronics(self):
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.electronics)))

    """Actions"""

    def click_menu(self):
        self.get_menu().click()
        print('Открыли меню')
    def click_electronics(self):
        self.get_electronics().click()
        print('Выбрали раздел электроника')

    """Methods"""

    def select_electronics(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_menu()
        self.click_electronics()
