class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 截图
    def save_picture(self,filepath):
        self.driver.save_screenshot(filepath)