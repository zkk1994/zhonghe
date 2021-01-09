'''
脚本层的一些公共方法
'''
import os
import sys

import pytest

from ZongHe.caw import DataRead


from ZongHe.caw.BaseRequests import BaseRequests

def get_project_path():
    '''
    获取工程路径
    :return: 当前工程路径，比如E:\ApiAutoTest\ZongHe\
    '''
    # __file__ 存储着当前文件的路径
    path = os.path.realpath(__file__)
    # 上一级目录
    path = os.path.dirname(path)
    # 再上一级目录
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    return path + "\\"
# python包的搜索路径：当前路径、Python安装路径、当前工程路径
print(get_project_path())
sys.path.append(get_project_path())

# 从环境文件中读环境信息,整个过程读一次即可
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini('data_env/env.ini',"url")

# 创建一个BaseRequests的实例，整个执行过程使用这个实例下发请求
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()

# 从环境文件中读db信息,整个过程读一次即可
@pytest.fixture(scope='session')
def db():
    # 读取出来是字符串，需要的是个字典，需要将字符串解析成字典
    info = DataRead.read_ini('data_env/env.ini',"db")
    print("================",type(info))
    print("================",type(eval(info)))
    return eval(info) # 将字符串解析成字典