"""
   ==============================================
    objectName： autoTestProject
    fileName：   TestLoginApply
    Author:      Hang
    Date:        2020/3/17/017
    description:  放箱申请系统 登录页面
   ==============================================

"""
import unittest

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from tools.utils import DriverUtil


class ApplyForLoginPage(BasePage):
    """申请系统 - 对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类浏览器对象
        self.login_input = (By.XPATH, "//input[@placeholder='请输入手机号']")
        self.password_input = (By.XPATH, "//input[@placeholder='请输入密码']")
        self.login_btn = (By.XPATH, "//div[@class='sumbit']//span")

    def find_account_input(self):
        """定位账号输入框"""
        return self.find_element_func(self.login_input)

    def find_password_input(self):
        """定位账号输入框"""
        return self.find_element_func(self.password_input)

    def find_login_btn(self):
        """定位账号输入框"""
        return self.find_element_func(self.login_btn)


class ApplyForLoginHandle(BaseHandle):
    """申请系统 - 操作层"""

    def __init__(self):
        self.login_page = ApplyForLoginPage()  # 获取元素定位对象

    def input_account(self, account):
        """输入账号"""
        self.input_text(self.login_page.find_account_input(), account)

    def input_password(self, password):
        """输入密码"""
        self.input_text(self.login_page.find_password_input(), password)

    def click_login_btn(self):
        """点击登陆"""
        self.login_page.find_login_btn().click()


class LoginProxy(object):
    """申请系统 - 业务层"""

    def __init__(self):
        self.login_handle = ApplyForLoginHandle()

    def login(self, account, password):
        """登录的业务"""
        self.login_handle.input_account(account)  # 输入账号
        self.login_handle.input_password(password)  # 输入密码
        self.login_handle.click_login_btn()  # 点击登录
