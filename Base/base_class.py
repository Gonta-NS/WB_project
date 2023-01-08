import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        current_url = self.driver.current_url
        print('Current url = ' + current_url)


    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot = 'screenshot ' + str(now_date) + '.png'
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\DEMO_projects\\WB_project\\Screen\\' + screenshot)


