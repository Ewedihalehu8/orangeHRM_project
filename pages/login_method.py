from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_public_method import BasePage
from pages.login_locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    # 1.输入用户名
    def enter_username(self, username):
        # 智能等待加载这个元素
        #等待加载用户名这个文本框
        WebDriverWait(self.driver,10).until(
            lambda driver:driver.find_element(*LoginPageLocators.username_text))
        # 用户名元素定位，加*是将元组格式拆成两个参数
        element = self.driver.find_element(*LoginPageLocators.username_text)
        element.click()
        element.clear()
        element.send_keys(username)
    # 2.输入密码
    def enter_password(self, password):
        WebDriverWait(self.driver,10).until(
            lambda driver:driver.find_element(*LoginPageLocators.password_text))
        element = self.driver.find_element(*LoginPageLocators.password_text)
        element.clear()
        element.send_keys(password)
    # 3.单击登录
    def click_login(self):
        element = self.driver.find_element(*LoginPageLocators.login_button)
        element.click()
    # 4.返回要验证的文本，登录成功
    def result_login_success(self):
        # 验证元素
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(MainPageLocators.user_name))
        return self.driver.find_element(*MainPageLocators.user_name).text