#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 连接数据库 类似java jdbc操作

import MySQLdb
from DBUtils.PooledDB import PooledDB

try:
    # 获取数据库连接
    conn = MySQLdb.connect(host='localhost',
            port = 3306,
            user='root',
            passwd='123456',
            db ='project',);
    # 获取游标
    cursor = conn.cursor()
    cursor.execute('insert into t_shiro_permission(c_name,c_url,c_identity,t_createtime) '
                   'VALUES (%s,%s,%s,NOW())',("hehe2","sdfsdf2","sdfsdf2"))
    data = cursor.fetchall()
    print data
    cursor.close()
    # 提交事务
    conn.commit()
except Exception as e:
    # 回滚
    conn.rollback()
    print e.message
finally:
    # 关闭连接
    conn.close()

# 配置连接池
def getDBPool():
    pool =  PooledDB(MySQLdb, 5, host='localhost', user='root', passwd='123456', db='project', port=3306)
    conn = pool.connection()

getDBPool()