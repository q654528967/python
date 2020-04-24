import json
data = [
    {'d1': '好', 't': 1},
    {'d1': '看', 't': 2},
    {'d1': '和', 't': 3},
    {'d1': '的', 't': 4}
]
d1 = json.dumps(data)
# print(d1)
d2 = json.loads(d1)
# print(d2)
with open('test.json', 'r', encoding='utf-8') as fp:
    d3 = json.load(fp)
    print(d3)
