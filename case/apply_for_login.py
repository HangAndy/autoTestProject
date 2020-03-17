# coding=gbk
"""
   ==============================================
    objectName�� autoTestProject
    fileName��   apply_for_login
    Author:      Hang
    Date:        2020/3/17/017
    description: ��������ϵͳ��¼��������
   ==============================================

"""
import unittest

from page.apply_for_system.apply__for_login_page import LoginProxy
from tools.utils import DriverUtil


class TestApplyForLogin(unittest.TestCase):

    @classmethod
    def account_info(cls):
        # ��ȡ��¼��Ϣ
        # account_info_dict = DriverUtil.get_account_info("�˺�.json")
        # print(account_info_dict)
        # cls.account = account_info_dict[1]
        # cls.password = account_info_dict[2]
        cls.account = "18915761068"
        cls.password = "123456"

    @classmethod
    def setUpClass(cls) -> None:
        cls.account_info()
        cls.driver = DriverUtil.get_driver()  # ��ȡ���������
        cls.driver.implicitly_wait(6)
        cls.driver.get('http://218.4.219.83:8099/webfleet')
        cls.login_proxy = LoginProxy()  # ��¼ҳ��ҵ��ִ�ж���

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # �˳����������

    def test_login(self):
        """��¼���Է���"""
        self.login_proxy.login(self.account, self.password)
