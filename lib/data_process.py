import pymysql
import const
import pandas as pd


# 连接到数据库的函数，带一个默认参数
def connect(db_name=const.db_name):
    con = pymysql.connect(host=const.host_t, port=const.port_t,
                          user=const.user_t, passwd=const.pwd, db=const.db_name)
    # 返回一个connection对象
    return con


# 执行SQL语句的函数，有无需要返回结果都可以使用这个函数
def sql_exec(sql):
    con = connect()
    cur = con.cursor()
    cur.execute(sql)
    ret = pd.DataFrame(cur.fetchall())
    result = [tuple(row) for row in ret.values]
    # 把从数据库里获取来的记录转换成元组然后返回过来
    # 提交事务
    con.commit()
    cur.close()
    con.close()
    return result
