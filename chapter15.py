import pymysql

connect = pymysql.connect(host='127.0.0.1',
                user='root',
                password='root',
                port=3306,
                db='chapter01',
                charset='utf8')
cur = connect.cursor()
sql = 'select * from sys_user'
cur.execute(sql)
data = cur.fetchall()
for i in data:
    print(i)
cur.close()