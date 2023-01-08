from selenium import webdriver
from Pages.main_page import Main_page
from Pages.electronics_page import Electronics_page
from Pages.laptops_page import Laptops_page
from Utilities.conftest import set_up
from Pages.cart_page import Cart_page


def test_select_laptop(set_up):
    driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\browser_driver\\chromedriver.exe\\')

    mp = Main_page(driver)
    mp.select_electronics()
    ep = Electronics_page(driver)
    ep.select_laptops()
    lp = Laptops_page(driver)
    lp.select_laptop()
    cp = Cart_page(driver)
    cp.check_selection()


