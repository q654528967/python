from selenium import webdriver
from lxml import etree
import pymongo


class LagouSpider(object):
    driver_path = r'E:\chromedriver_win32\chromedriver.exe'
    client = pymongo.MongoClient('127.0.0.1', port=27017)

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=LagouSpider.driver_path
        )
        self.base_url = 'https://gangkou.51240.com'
        self.dblist = LagouSpider.client.list_database_names()
        self.db = LagouSpider.client['hs_test']
        self.collist = self.db.list_collection_names()
        self.table_key = ''

    def run(self):
        self.driver.get(self.base_url)
        source = self.driver.page_source
        if 'hs_test' in self.dblist:
            print('数据库连接成功')
        if 'tables' in self.collist:
        #     self.db['tables'].drop()
            print('表有了')
        self.parse_list_page(source)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        values = html.xpath(""".//tbody//tr/td/a/@href""")
        for value in values:
            url = self.base_url+value
            print(url)
        self.driver.close()


if __name__ == "__main__":
    spider = LagouSpider()
    spider.run()
