# coding=gbk
import time
import unittest

from case.apply_for_login import TestApplyForLogin
from tools.HTMLTestRunnerCN import HTMLTestReportCN
from tools.utils import DriverUtil

suite = unittest.TestSuite()  # ��ʼ���׼�����

# ���÷�����װ��������
suite.addTest(unittest.makeSuite(TestApplyForLogin))
# �ر�������˳�����
DriverUtil.change_quit_status(False)
# TODO: ���ɲ��Ա���(��Ҫע�͵� TextTestRunner() ����)
now_time = time.strftime('%Y%m%d_%H%M%S')  # ��ȡ��ǰʱ��
# ��ʼ������ִ�ж��󲢵��÷���
unittest.TextTestRunner().run(suite)
# ���ñ�������Ϣ

time.sleep(20)
