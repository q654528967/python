import json
import pymongo

client = pymongo.MongoClient('127.0.0.1', port=27017)
col = client['hs_test']['us_hs_list_item']
datas = open('htsdata.json', encoding='utf-8')
datas = json.load(datas)
for data in datas:
    col.insert_one(data)

