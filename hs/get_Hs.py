import requests
from lxml import etree
import pymongo


class GetHs(object):
    client = pymongo.MongoClient('127.0.0.1', port=27017)

    def __init__(self):
        self.base_url = 'http://www.hs-bianma.com/'
        self.dblist = GetHs.client.list_database_names()
        self.db = GetHs.client['hs_test']
        self.collist = self.db.list_collection_names()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.'
                          '3987.149 Safari/537.36'
        }

    def run(self):
        if 'hs_test' in self.dblist:
            print('数据库连接成功')
        if 'hs_list_item' in self.collist:
            code = input("hs_list_item 在数据库, 是否删除,(y删除)")
            if code == 'y':
                self.db['hs_list_item'].drop()
            else:
                pass
        response = requests.get(self.base_url, headers=self.headers)
        text = response.content.decode('utf-8')
        html = etree.HTML(text)
        a_hrefs = html.xpath("""//div[@id="div_catalog"]/div[starts-with(@id,"con")]//a/@href""")
        self.headers['Referer'] = 'http://www.hs-bianma.com/'

        for a_href in a_hrefs:
            url = self.base_url + a_href
            self.open_sub(url)

    def open_sub(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.content.decode('utf-8')
        html = etree.HTML(text)
        ths = html.xpath("""//th/text()""")
        trs = html.xpath("""//tr""")[1:]
        for tr in trs:
            tds = tr.xpath(""".//td/text()""")
            table_data = dict(zip(ths, tds))
            self.db['hs_list_item'].insert_one(table_data)


if __name__ == '__main__':
    get_hs = GetHs()
    get_hs.run()
