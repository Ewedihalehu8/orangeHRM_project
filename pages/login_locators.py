from selenium.webdriver.common.by import By

# 登录页元素及定位方式
class LoginPageLocators(object):
    # 登录用户名的元素定位，采用元组形式，通过CLASS_NAME定位
    username_text = (By.NAME, 'username')
    password_text = (By.NAME, 'password')
    login_button = (By.XPATH,'//button[@type="submit"]')

# 主页元素定位及方式
class MainPageLocators(object):
    user_img = (By.CLASS_NAME,"oxd-userdropdown-img")
    user_name = (By.CLASS_NAME,"oxd-userdropdown-name")
    # 管理员按钮
    admin_button = (By.XPATH,'//span[contains(@class,"oxd-text oxd-text--span oxd-main-menu-item--name")]')
    # 工作按钮
    job_list = (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent']")
    #职称按钮
    job_title = (By.XPATH,"//ul[contains(@class,'oxd-dropdown-menu')]//a[text()='职称']")
    # q =         (By.XPATH,"//ul[contains(@class,'oxd-dropdown-menu')]//a[text()='职称']")