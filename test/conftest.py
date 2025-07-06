import os
import sys
from selenium.webdriver.chrome.service import Service
import allure,pytest
from selenium import webdriver
from utils.get_path import get_par_path
from utils.log import conf
from utils.read_yaml import get_yaml_data

sys.path.append('../..')
@allure.feature("打开浏览器")
@pytest.fixture(scope="session")
def init_driver(request):
    log = conf.logcon()
    log.info('setup_class')
    driver_path = os.path.join(get_par_path(),'/usr/local/bin/chromedriver')
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    # yield driver
    # driver.quit()
    def close_browser():
        driver.quit()
        request.addfinalizer(close_browser)
    # # 无论执行正确还是错误最终都关闭浏览器
    return driver

# @allure.step("从配置文件中读取登录数据")
@pytest.fixture
def login_data():
    # log = conf.logcon()
    # log.info("read config.yaml")
    yaml_path = os.path.join(get_par_path(),"config/config.yaml")
    print("YAML path:", yaml_path)
    test_data = get_yaml_data(yaml_path)
    print("Loaded data type:", type(test_data))
    print("Loaded data content:", test_data)
    return test_data
    # return {
    #     "baseURL": "http://localhost/orangehrm-5.7",
    #     "username": "zxtzxt",
    #     "password": "Zxt295470@"
    # }

# @allure.step("0:这是初始化数据")
@pytest.fixture
def get_data(request):
    value = request.param
    print("get_data fixture value",value)
    return value

