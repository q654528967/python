import csv

header = ['name', 'age', 'height']
value = [
    {'name': '招生', 'age': 18, 'height': 65},
    {'name': '历史', 'age': 22, 'height': 45},
    {'name': '欢迎', 'age': 45, 'height': 75}
]
with open('write1.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.DictWriter(fp, header)
    writer.writeheader()
    writer.writerows(value)
