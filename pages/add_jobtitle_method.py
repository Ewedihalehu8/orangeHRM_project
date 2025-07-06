from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_public_method import BasePage
from pages.job_title_locators import AddJobTitleLocators
from pages.login_locators import MainPageLocators


class AddJobtilePage(BasePage):
    # 进入job页面
    def click_movetoelemnt_job(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver:driver.find_element(*MainPageLocators.admin_button))
        self.driver.find_element(*MainPageLocators.admin_button).click()
        self.driver.find_element(*MainPageLocators.job_list).click()
        self.driver.find_element(*MainPageLocators.job_title).click()

    # 1.单击添加职称按钮
    def click_add_jobtitle(self):
        element_click = self.driver.find_element(*AddJobTitleLocators.add_jobtile_button)
        element_click.click()

    # 2.输入职称
    def enter_jobTitle(self, jobTitle):
        # 智能等待加载这个元素
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(*AddJobTitleLocators.job_titleName))
        element = self.driver.find_element(*AddJobTitleLocators.job_titleName)
        element.click()
        element.clear()
        # 输入内容
        element.send_keys(jobTitle)

    # 3.输入工作描述
    def enter_jobDescription(self, jobDescription):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*AddJobTitleLocators.job_description))
        element = self.driver.find_element(*AddJobTitleLocators.job_description)
        element.send_keys(jobDescription)

    # 4.输入注释文本
    def enter_note_text(self, noteText):
        WebDriverWait(self.driver, 10).until(
            lambda driver:driver.find_element(*AddJobTitleLocators.job_note))
        element = self.driver.find_element(*AddJobTitleLocators.job_note)
        element.send_keys(noteText)

    # 5.单击确定
    def click_addjobtitle_submit(self):
        element_click = self.driver.find_element(*AddJobTitleLocators.job_title_submit)
        element_click.click()

    # 6.返回要验证的文本
    def result_addjobtitle_sucess(self):
        # WebDriverWait(self.driver, 10).until(
        #     EC.url_contains("admin/viewJobTitleList"))
        # return self.driver.current_url
        if "viewJobTitleList" in self.driver.current_url:
            return True