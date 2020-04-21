import pymongo
from bson.objectid import ObjectId


client = pymongo.MongoClient('127.0.0.1', port=27017)
mydb = client['hs_test']
mycol = mydb['tables']
mo_id = {"港口名(中文)": "圣克鲁斯"}

result = mycol.find(mo_id)
resss = list(result)
print(resss)
print(len(resss))

