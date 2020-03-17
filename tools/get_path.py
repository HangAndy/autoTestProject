"""
   ==============================================
    objectName： Projrct_1
    fileName：   get_path
    Author:      Hang
    Date:        2020/3/16/016
    description: 获取绝对路径
   ==============================================

"""
import os


def get_path():
    func_path = os.path.dirname(__file__)  # 获取当前脚本所在目录的绝对路径
    base_dir = os.path.dirname(func_path)  # 获取当前脚本的上一级目录的绝对路径，可以多次获取上一级目录
    base_dir = str(base_dir)  # 以字符串方式来处理
    base_dir = base_dir.replace('/', '\\')
    return base_dir


if __name__ == '__main__':
    get_path()
