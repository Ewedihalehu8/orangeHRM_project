from selenium.webdriver.common.by import By


class AddJobTitleLocators:
    # 添加职称按钮
    add_jobtile_button = (By.XPATH, '//button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary")]')
    # 职称输入框
    job_titleName = (By.XPATH, '//div[contains(@class,"oxd-input-group oxd-input-field-bottom-space")]//input['
                               'contains(@class,"oxd-input oxd-input--active")]')
    # 职位描述
    job_description = (By.XPATH,'//div[contains(@class,"oxd-form-row")]//textarea[contains(@class,"oxd-textarea '
                                'oxd-textarea--active oxd-textarea--resize-vertical")]')
    # # 工作规范
    # job_rule = (By.XPATH,'//div[contains(@class,"oxd-form-row")]//div[contains(@class,"oxd-file-button"]')
    # 注释
    job_note = (By.XPATH,'//div[contains(@class,"oxd-input-group oxd-input-field-bottom-space")]//textarea[contains(@class,"oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical")]')
    # 提交按钮
    job_title_submit = (By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space")]')