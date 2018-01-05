#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 python 主流数据库操作框架 SQLAIchemy
 orm数据库框架 类似java mybatis jpa hibernate等框架

 mysql://root:pass/test
    root是用户名 pass密码 test数据库
    session相当于MySQLdb里面的游标
    first 相当于fetchone
    echo=True 会输出所有的sql

注意：使用fetch后连接会被自动关闭
"""
import time

import MySQLdb
from DBUtils.PooledDB import PooledDB
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy.types import *

engine = create_engine('mysql://root:123456@localhost/project', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
ret = session.execute("select 1")
# print ret.first()
print ret.fetchall()

print '---------------------orm映射实体demo分割线--------------------'

'获取数据库session pool配置见create_engine.__init___'

def getSession():
    engine = create_engine('mysql://root:123456@localhost/project',
                           encoding="utf-8",
                           echo=True,
                           pool_size=10)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


BaseModel = declarative_base()


# sqlalchemy.types里面有所有的数据字段类型，等于sql类型的大写
# 注意：python 中是区分大小写的
# 实体与数据库映射关系
class Permission(BaseModel):
    __tablename__ = "t_shiro_permission"  # 表名
    id = Column('n_id', INT(), primary_key=True)
    name = Column('c_name', VARCHAR(10), default=null, nullable=False)
    url = Column('c_url', VARCHAR(255), default=null, nullable=False)
    identity = Column('c_identity', VARCHAR(255), default=null, nullable=False)
    createTime = Column('t_createtime', TIMESTAMP())
    status = Column('n_status', INT(), default=0)

    def __init__(self, name, url, identity, status):
        self.name = name
        self.url = url
        self.identity = identity
        self.status = status

    def __str__(self):
        return 'Permission:[name=' + self.name + ',id=' + \
               str(self.id) + ',identity=' + self.identity + \
               ',url=' + self.url + ',createTime=' + \
               str(self.createTime) + ']'


# insert操作
def insertPermission():
    p1 = Permission("fuck", "http://www.baidu.com", "ABC123", 0)
    session = getSession()
    session.add(p1)
    session.commit()
    print p1.id


# insertPermission()

# 查询操作
def queryPermission():
    session = getSession()
    query = session.query(Permission)
    print '根据主键查询：'
    print query.get(2)  # 根据主键ID查询
    # 条件查询
    #         1.[and] 多个条件，用多个filter
    #         2.[and] filter(User.id > 1, User.name != 'a')
    #         3.[or] or_(User.id == 1, User.id == 2)
    #         4.[in] User.id.in_((1, 2))
    #         5.[is null] filter('name is null')
    #         6.[not] filter(not_(User.name == None))
    #         7.filter("user_name = 'lujianxing' and accout=1245678")
    #
    #         注意：filter中可以直接使用数据库表字段操作
    #               也可以用定义的类字段操作
    print '根据条件查询（多个条件，用多个filter）：'
    result = query.filter(Permission.name == 'fuck').filter(Permission.id == 4).all()
    print result.__len__()
    print result[0]
    print '分页查询：'
    # order_by 排序
    #              1. 对象属性 order_by(Permission.createTime.desc())
    #              2. 数据库表字段 order_by("t_createtime desc")
    # offset 记录数
    # limit 页面大小
    print query.filter(Permission.name == 'fuck').order_by("t_createtime desc").\
            offset(1).limit(1).all()[0]

    print '------------------数据库聚合函数使用------------------'
    print session.query(func.count('*')).select_from(Permission).scalar()
    print session.query(func.count('1')).select_from(Permission).all()
    print session.query(func.count(Permission.id)).scalar() # filter() 中包含 Permission，因此不需要指定表

# queryPermission()

# 更新操作
def updatePermission():
    session = getSession()
    query = session.query(Permission)
    print query.get(4)
    # 更新方式一：update方式
    print 'update方式更新数据'
    query.filter(Permission.id==4).update({Permission.name:'fuck2'})
    print query.get(4)
    session.commit()

    # 更新方式二：赋值方式
    print '赋值方式更新数据'
    p2 = query.get(4);
    p2.name = 'fk'
    session.commit()
    session.close()

# updatePermission()

# 删除操作
'''
问题：sqlalchemy如何批量删除多条数据
解决：使用参数synchronize_session=False，或for循环
方法：
        users = self.db.query(User).filter(User.id.in_(1,2,3)).all()
        [self.db.delete(u) for u in users]
        self.db.commit()
或
        users = self.db.query(User).filter(User.id.in_(1,2,3)).delete(synchronize_session=False)
        self.db.commit()
'''
def deletePermission():
    session = getSession()
    query = session.query(Permission)
    ret = query.get(5)
    session.delete(ret);
    session.commit()

deletePermission()