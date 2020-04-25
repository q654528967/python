import pymysql
conn = pymysql.connect(host='localhost', user='root', port=3306, password='', database='python')
cursor = conn.cursor()
sql = """insert into test(id,name,age,password) values(null,'cbb',22,111)"""
cursor.execute(sql)
conn.commit()
result = cursor.fetchone()
print(result)
conn.close()
