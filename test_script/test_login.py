'''
登录接口测试脚本
'''

import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml("data_case/login_setup.yaml"),scope='module')
def setup_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml("data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture(scope='module')
def register(setup_data, db, url, baserequests):
    # 注册用户
    mobile = setup_data['casedata']['mobilephone']
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.delete_user(db, mobile)


def test_login(register, login_data, url, baserequests):
    # 下发登录的请求
    r = Member.login(url, baserequests, login_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == login_data['expect']['msg']
    assert str(r.json()['code']) == str(login_data['expect']['code'])
