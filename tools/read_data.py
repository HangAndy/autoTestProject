"""
   ==============================================
    objectName： autoTestProject
    fileName：   read_data
    Author:      Hang
    Date:        2020/3/17/017
    description: 用来读取本地文件数据
   ==============================================

"""
import json

from tools.get_path import get_path


# def write_json():
#     keys = {
#         '放箱申请系统': ("http://218.4.219.83:8099/webfleet", "18915761068", "123456"),
#         '放箱审批系统': ("http://218.4.219.83:8099/webship", "13913564273", "123456"),
#         '堆场管理系统': ("http://218.4.219.83:8099/webyard", "13616223598", "123456"),
#         '码头系统': ("http://218.4.219.83:8099/login/wharf", "18262661928", "123456")
#     }
#     with open(get_path() + '\\data\\' + "账号.json", 'w', encoding="gbk")as fp:
#         return fp.write(json.dumps(keys, ensure_ascii=False))

def read_data(text_name):
    """
    用来读取本地文件数据
    :param text_name: 文件名
    :return: dict
    """

    return json.load(open(get_path() + '\\data\\' + text_name, 'r', encoding="gbk"))


if __name__ == '__main__':
    dict_account = read_data("账号.json")
    print(dict_account)
    print(type(dict_account))
