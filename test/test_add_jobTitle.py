import logging
from datetime import datetime, time
import os.path
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.add_jobtitle_method import AddJobtilePage
from pages.base_public_method import BasePage
from pages.login_method import LoginPage
from utils.get_path import get_par_path
from utils.log import conf
from utils.read_yaml import get_yaml_data
# from test.conftest import init_driver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with allure.step("0.从数据文件中读取添加职称数据信息"):
    yaml_path = os.path.join(get_par_path(),"datafile/addjob_data.yaml")
    test_data = get_yaml_data(yaml_path)
    print("test_data:", test_data)

class TestAddJobTitle(object):
    # 登录
    @allure.feature("登录功能")
    @allure.step("使用zxtzxt身份登录")
    def test_login(self,init_driver,login_data):
        # log = conf.logcon()
        # log.info("login")
        # self.log.info("login")
        init_driver.get(login_data["baseURL"] + "/web/index.php/auth/login")
        init_driver.maximize_window()
        init_driver.implicitly_wait(30)
        base_page = BasePage(init_driver)
        with allure.step("初始化登录项"):
            login_page = LoginPage(init_driver)
        with allure.step("输入用户名密码后单击登录"):
            login_page.enter_username(login_data["username"])
            login_page.enter_password(login_data["password"])
            login_page.click_login()
        with allure.step("断言是否登录成功并截图"):
            assert 'xiang xiang' in login_page.result_login_success()
            pic_path = os.path.join(get_par_path(),"shootpicture/")
            base_page.save_picture(pic_path+str(datetime.now()) + 'login.png')
    # 添加职称
    @allure.feature("添加职称功能")
    @pytest.mark.parametrize("job_data",test_data)
    def test_add_jobTitle(self,init_driver,job_data):
        job = job_data['case']
        jobTitle = job['jobTitle']
        jobDescription = job['jobDescription']
        noteText = job['noteText']
        base_page = BasePage(init_driver)
        addjobtitle_page = AddJobtilePage(init_driver)
        with allure.step("1.进入职称页"):
            addjobtitle_page.click_movetoelemnt_job()
            addjobtitle_page.click_add_jobtitle()
        with allure.step("2.输入信息"):
            addjobtitle_page.enter_jobTitle(jobTitle)
            addjobtitle_page.enter_jobDescription(jobDescription)
            addjobtitle_page.enter_note_text(noteText)
        with allure.step("3.提交保存"):
            addjobtitle_page.click_addjobtitle_submit()
        with allure.step("4.等待页面渲染完成"):
            WebDriverWait(init_driver,10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{jobTitle}')]")))
        with allure.step("5.断言成功并截图"):
            # 断言1:验证URL是否正确
            expected_url = "http://localhost/orangehrm-5.7/web/index.php/admin/viewJobTitleList"
            WebDriverWait(init_driver, 10).until(
                EC.url_to_be(expected_url)
            )
            # assert expected_url == init_driver.current_url,f"期望URL: {expected_url}, 实际URL: {init_driver.current_url}"
            # 断言2:验证页面标题包含职称
            # assert jobTitle in init_driver.page_source
            WebDriverWait(init_driver,10).until(
                EC.text_to_be_present_in_element((By.XPATH,"//h6[contains(@class,'orangehrm-main-title')]"),
                "职称" ))
            # 断言3:验证记录数量增加
            # records_found = init_driver.find_element(
            #     By.XPATH,"//div[contains(@class,'orangehrm-horizontal-padding orangehrm-vertical-padding')]//span[contains(@class,'oxd-text oxd-text--span') and coantains(text(),'Records Found')]"
            # ).text
            # assert "Records Found" in records_found
            # 断言4:验证职称是否存在与列表中
            job_title = f"//*[contains(text(), '{jobTitle}')]"
            WebDriverWait(init_driver,15).until(
                EC.visibility_of_element_located((By.XPATH,job_title))
            )
            # base_page.hightlight_element(job_title_element)

            # assert jobTitle in init_driver.page_source
            # print("页面标题:", init_driver.title)
            # print("当前URL:", init_driver.current_url)
            # print("页面元素:", init_driver.find_element(By.TAG_NAME, "body").text[:500])

            pic_path = os.path.join(get_par_path(),"shootpicture/")
            pic_name = pic_path+str(datetime.now()) + '_addjob.png'
            base_page.save_picture(pic_name)
            allure.attach.file(pic_name,attachment_type=allure.attachment_type.PNG)

