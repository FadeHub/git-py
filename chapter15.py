import pymysql

connect = pymysql.connect(host='127.0.0.1',
                user='root',
                password='root',
                port=3306,
                db='chapter01',
                charset='utf8')
cur = connect.cursor()
#sql 查询
sql = 'select * from sys_user'
cur.execute(sql)
data = cur.fetchall()
for i in data:
    print(i)
insert_sql = """insert into sys_user(username,password) values('李四','2033')"""
#sql插入
try:
    cur.execute(insert_sql)
    connect.commit()
except:
    connect.rollback()
cur.close()