#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='sqlexample')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
# effect_row = cursor.execute("insert into class(caption) values('五年三班')")
# print(effect_row)


#插入单个
#info = input("请输入班级：")
#effect_row = cursor.execute('insert into class(caption) values (%s)',info)


#插入一条多个
# r = cursor.execute('insert into student(gender,class_id,sname) values(%s,%s,%s)' ,('女','1','鸭蛋'))
# # 提交，不然无法保存新建或者修改的数据
# conn.commit()


#插入多条多个(可迭代的数组)


# W = [
#     ('女',1,'鸭蛋1'),
#     ('女',1,'鸭蛋2'),
#     ('女',1,'鸭蛋3'),
# ]
#
#
# r = cursor.executemany('insert into student(gender,class_id,sname) values (%s,%s,%s)',W)
# conn.commit()


# #更新
# r = cursor.execute('update student set sname = "龙傲天" where class_id = 8')
# conn.commit()

# #删除
# d = cursor.execute('delete from score where sid = %s',(52,))
# conn.commit()

#查询

s = cursor.execute('select * from student')
# result = cursor.fetchall()
# result = cursor.fetchone()
result = cursor.fetchmany(3)
print(result)
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()