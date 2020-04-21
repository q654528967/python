import requests
import pymongo
from bs4 import BeautifulSoup

init_url = 'https://gangkou.51240.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36'
}
data = []
client = pymongo.MongoClient('127.0.0.1', port=27017)
dblist = client.list_database_names()
if 'hs_test' in dblist:
    print('数据库连接成功')
mydb = client['hs_test']
collist = mydb.list_collection_names()
if 'tables' in collist:
    mydb['tables'].drop()
table_key = ''


# 遍历第一层页面tr下的td ，返回td的数据列表
def get_td(input_data):
    tr_data = {'tr': []}
    for td in input_data:
        td_data = []
        if not td.has_attr('bgcolor'):
            a_tag = td.a.extract()
            a_text = a_tag.get_text()
            td_data.append(a_text)
            a_href = init_url + a_tag['href']
            open_suburl(a_href)
        td_str = td.string
        td_data.append(td_str)
        tr_data['tr'].append(td_data)
    return tr_data


# 遍历第一层页面trs，返回整个table的数据
def get_tr(input_data):
    table_data = []
    for tr in input_data:
        tds = tr.find_all('td')
        table_data.append(get_td(tds))
    return table_data


# 打开二级页面下的tds,返回一个tr的数据
def open_subtd(input_data):
    tr_data = {'tr': []}
    for key, td in enumerate(input_data):
        td_data = []
        if key == 0:
            a_tag = td.a.extract()
            a_href = init_url + a_tag['href']
            text = requests.get(a_href, headers=headers).content.decode('utf-8')
            soup = BeautifulSoup(text, 'html5lib')
            trs = soup.select('#fcj_jg table tr')
            result = {}
            for tr in trs:
                res = list(tr.stripped_strings)
                if len(res) == 2:
                    result[res[0]] = res[1]
                else:
                    result[res[0]] = ''
            mydb['tables'].insert_one(result)
        else:
            tt = td.get_text()
            if not(tt == ''):
                td_str = list(td.stripped_strings)[0]
                td_data.append(td_str)
    return tr_data


# 遍历二级页面的trs，返回二级页面table的数据
def open_subtr(input_data):
    table_data = []
    for tr in input_data:
        tds = tr.find_all('td')
        table_data.append(open_subtd(tds))
    return table_data


# 打开二级页面，接受二级页面的数据，并插入数据库
def open_suburl(input_url):
    if table_key == 'table0':
        response = requests.get(input_url, headers=headers).content.decode('utf-8')
        soup = BeautifulSoup(response, 'html5lib')
        trs = soup('table', attrs={
            'width': '100%'
        })[0].tbody.find_all('tr')[1:]
        datas = open_subtr(trs)
        return datas


def main():
    response = requests.get(init_url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    tables = soup('table', attrs={
        'width': '95%',
        'border': 0,
        'cellpadding': 2
    })
    for key, table in enumerate(tables):
        global table_key
        table_key = 'table%s' % key
        table_data = {table_key: []}
        trs = table.tbody.find_all('tr')[1:]
        table_data[table_key] = get_tr(trs)
        data.append(table_data)
    print('数据爬取完成')
    # print(data)
    # 插入数据
    # 判断集合是否存在

    if 'select_table' in collist:
        mydb['select_table'].drop()
        mydb['select_table'].insert_many(data)


if __name__ == '__main__':
    main()
