import csv

header = ['name', 'age', 'height']
value = [
    ('招生', 18, 65),
    ('历史', 22, 45),
    ('欢迎', 45, 75)
]
with open('write.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(header)
    writer.writerows(value)
