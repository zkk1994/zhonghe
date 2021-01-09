'''
操作数据库
'''

from ZongHe.caw import Mysql

# 比如后续版本优化，将数据库从mysql换成sqlite了，
def delete_user(db,mobile):
    '''
    根据手机号码删除注册用户
    :param db: 数据库信息，字典格式的
    :param mobile: 手机号码
    :return:
    '''
    conn = Mysql.connect(db)
    mobile = "13412145678"
    sql = f"delete from member where mobilephone={mobile}"
    Mysql.execute(conn,sql)
    Mysql.disconnect(conn)

def query_user(db,mobile):
    '''
    根据手机号码查询注册用户
    :param db: 数据库信息，字典格式的
    :param mobile: 手机号码
    :return:
    '''
    conn = Mysql.connect(db)
    mobile = "13412145678"
    sql = f"select mobilephone from member where mobilephone={mobile}"
    Mysql.execute(conn,sql)
    Mysql.disconnect(conn)
