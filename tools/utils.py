"""
公共方法
"""
import time
from selenium import webdriver


class DriverUtil(object):
    """浏览器工具类"""
    _driver = None  # 为了表示浏览器对象的初始化状态(判断条件无法表示对象状态)
    _status = True  # 浏览器退出方法开关属性

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了保证获取的浏览器对象始终是同一个, 需要条件判断浏览器对象的状态
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 需要判断浏览器对象存在再执行退出操作
        if cls._driver and cls._status:
            cls._driver.quit()
            cls._driver = None  # 保险措施, 确保浏览器对象的初始化状态

    @classmethod
    def change_quit_status(cls, status):
        """修改退出状态方法"""
        cls._status = status


if __name__ == '__main__':
    DriverUtil.get_driver()
    time.sleep(2)
    DriverUtil.quit_driver()
