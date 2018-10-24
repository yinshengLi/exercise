#__author:iruyi
#date:2018/9/21
import pymysql

#打开数据库连接 host name password database-name
db = pymysql.connect('localhost', 'root', 'root', 'test')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version: %s' % data)

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEETT")
# # 创建表
# sql = '''CREATE TABLE EMPLOYEETT (
# FIRST_NAME  CHAR(20) NOT NULL,
# LAST_NAME  CHAR(20),
# AGE INT,
# SEX CHAR(1),
# INCOME FLOAT )'''
# cursor.execute(sql)

#sql 插入
# insertsql = '''INSERT INTO EMPLOYEETT(FIRST_NAME,
# LAST_NAME, AGE, SEX, INCOME)
# VALUES ('Mac', 'Mohan', 20, 'M', 2000)'''
#
# try:
#     cursor.execute(insertsql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()


# 查询
querysql = '''SELECT * FROM EMPLOYEETT WHER
INCOME > 1000
'''
try:
    # 执行SQL语句
    cursor.execute(querysql)
    query = cursor.fetchone()
    print(query)
except:
    print('Error: unalbe to fetch data')

# 更新
# updatesql = '''UPDATE EMPLOYEETT set AGE = AGE +1 WHERE INCOME > 0'''
#
# try:
#     # 执行sql语句
#     cursor.execute(updatesql)
#     # 提交到数据库执行
#     db.commit()
# except Exception as e:
#     print('出现异常，回滚', e)
#     db.rollback()

print('执行成功')
# 关闭数据库连接
db.close()