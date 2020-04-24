import requests
from lxml import etree
import pymongo


class InitData(object):
    client = pymongo.MongoClient('127.0.0.1', port=27017)

    def __init__(self):
        self.base_url = 'https://airport.supfree.net/index.asp?page='
        self.dblist = InitData.client.list_database_names()
        self.db = InitData.client['hs_test']
        self.collist = self.db.list_collection_names()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.'
                          '3987.149 Safari/537.36'
        }

    def run(self):
        if 'hs_test' in self.dblist:
            print('数据库连接成功')
        else:
            print('数据库连接失败')
        if 'jichang_list_item' in self.collist:
            self.db['jichang_list_item'].drop()
            print('表已丢弃')
        for i in range(1, 285):
            url = self.base_url + str(i)
            self.open_url(url)

    def open_url(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.content.decode('gbk')
        html = etree.HTML(text)
        trs = html.xpath("""//tr""")[1:]
        first_tr = html.xpath("""//tr[@class="xctd"]/td/text()""")
        for tr in trs:
            tds = tr.xpath(""".//td""")[1:]
            tds_list = []
            for td in tds:
                if td.text is None:
                    tds_list.append('')
                else:
                    tds_list.append(td.text)
            span_text = tr.xpath(""".//span/text()""")[0]
            tds_list.insert(0, span_text)
            table_data = dict(zip(first_tr, tds_list))
            self.db['jichang_list_item'].insert_one(table_data)


if __name__ == '__main__':
    getData = InitData()
    getData.run()
