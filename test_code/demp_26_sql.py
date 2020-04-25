import pymysql
db = pymysql.connect(host='localhost', user='root', port=3306, password='', database='python')
cursor = db.cursor()
# sql = """select name,password from test where id=0"""
# sql1 = """select * from test"""
sql1 = """delete from test where id=0"""
cursor.execute(sql1)
db.commit()
# res = cursor.fetchall()
# res = cursor.fetchone()
# res = cursor.fetchmany(1)
# print(res)
db.close()
