# coding=gbk
"""
   ==============================================
    objectName： autoTestProject
    fileName：   apply_for_login
    Author:      Hang
    Date:        2020/3/17/017
    description: 放箱申请系统登录测试用例
   ==============================================

"""
import unittest

from page.apply_for_system.apply__for_login_page import LoginProxy
from tools.utils import DriverUtil


class TestApplyForLogin(unittest.TestCase):

    @classmethod
    def account_info(cls):
        # 读取登录信息
        # account_info_dict = DriverUtil.get_account_info("账号.json")
        # print(account_info_dict)
        # cls.account = account_info_dict[1]
        # cls.password = account_info_dict[2]
        cls.account = "18915761068"
        cls.password = "123456"

    @classmethod
    def setUpClass(cls) -> None:
        cls.account_info()
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.driver.implicitly_wait(6)
        cls.driver.get('http://218.4.219.83:8099/webfleet')
        cls.login_proxy = LoginProxy()  # 登录页面业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def test_login(self):
        """登录测试方法"""
        self.login_proxy.login(self.account, self.password)
