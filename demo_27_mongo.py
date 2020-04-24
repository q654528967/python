import pymongo

client = pymongo.MongoClient('127.0.0.1', port=27017)

db = client.demo01_test
collection = db.qa
# testData = [
#     {'name': 'tang', 'age': 18},
#     {'name': 'tang', 'age': 18},
#     {'name': 'tang', 'age': 18},
#     {'name': 'tang', 'age': 18},
#     {'name': 'tang', 'age': 18},
# ]
# 插入一条数据
# x = collection.insert_one({'username': 'lei'})
# 插入多条数据
# collection.insert_many(testData)
# 查询全部数据
# cursor = collection.find()
# for x in cursor:
#     print(x)
# 查找一条数据
# cursor = collection.find_one()
# print(cursor)
# 带条件查找
# cursor = collection.find_one({'age': 18})
# print(cursor)
# 更新一条数据
# collection.update_one({'age': 38}, {'$set': {'age': 18}})
# 更新多条数据
# collection.update_many({'name': 'tang'}, {'$set': {'name': 'ping'}})
# 删除一条数据
# collection.delete_one({'uname': 'lei'})
# 删除多条数据
collection.delete_many({'username': 'lei'})
