import json
persons = [
    {'a': '按键', 'b': 'bh', 'c': 1},
    {'a': 'bb', 'b': 'bh', 'c': 2},
    {'a': '回来', 'b': 'bh', 'c': 3},
    {'a': 'ah', 'b': 'bh', 'c': 4},
]
# res = json.dumps(persons)
# print(res)
with open('test.json', 'w', encoding='utf-8') as fp:
    json.dump(persons, fp, ensure_ascii=False)
