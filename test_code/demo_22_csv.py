import csv


def read1():
    with open('csv_test.csv', 'r') as fp:
        reader = csv.reader(fp)
        next(reader)
        for x in reader:
            print(x)


def read2():
    with open('csv_test.csv', 'r') as fp:
        reader = csv.DictReader(fp)
        for x in reader:
            value = {'index': x['index'], 'county': x['county'], 'name': x['name'], 'code': x['code']}
            print(value)

            
read2()
