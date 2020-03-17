"""
   ==============================================
    objectName： Projrct_1
    fileName：   excle_func
    Author:      Hang
    Date:        2020/3/16/016
    description: Excel 读写操作操作
   ==============================================

"""

# 导包
import xlwt
import xlrd


from tools.get_path import get_path


def write_excel(name, dict_data):
    """
    创建一个Excel,并写入需要的内容
    这个内容应该是一个字典的格式  key:value
    :name: Excel 文件名
    :dict_data 写入的内容  例如(key:业务类型,value:进口)
    :return: None
    """
    new_workbook = xlwt.Workbook()  # 新建一个工作簿
    work_sheet = new_workbook.add_sheet("放箱数据导入")  # 新建一个工作表
    for index, i in enumerate(dict_data.items()):
        print(i[0], i[1])
        work_sheet.write(0, index, i[0])
        work_sheet.write(1, index, i[1])
    new_workbook.save(get_path() + "\data\\" + name)


if __name__ == '__main__':
    dic = {"1": "1", "2": "3"}
    write_excel("1.xlsx", dic)
