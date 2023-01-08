from Base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def check_selection(self):
        self.get_current_url()
        self.get_screenshot()


