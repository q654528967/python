from selenium import webdriver
from lxml import etree
import pymongo
import time

from selenium.common.exceptions import TimeoutException


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
        self.table_key = 0

    def run(self):
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)
        self.driver.get(self.base_url)
        source = self.driver.page_source
        if 'hs_test' in self.dblist:
            print('数据库连接成功')
        if 'tables' in self.collist:
            self.db['tables'].drop()
        self.parse_list_page(source)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        table = html.xpath("""//table""")[0]
        values = table.xpath("""./tbody//tr/td/a/@href""")
        for value in values:
            url = self.base_url+value
            self.driver.get(url)
            source = self.driver.page_source
            self.open_sub(source)

    def open_sub(self, source):
        html = etree.HTML(source)
        a_href = html.xpath("""//table[@width="100%"]/tbody//tr/td/a/@href""")
        for a in a_href:
            url = self.base_url+a
            try:
                self.driver.get(url)
            except TimeoutException:
                print('请求超时，将要停止加载了')
                self.driver.execute_script('window.stop()')
            source = self.driver.page_source
            self.open_sub_sub(source)
            time.sleep(1)

    def open_sub_sub(self, source):
        html = etree.HTML(source)
        trs = html.xpath("""//table[@width="100%"]/tbody//tr""")
        data = {}
        for tr in trs:
            td_f = tr.xpath(""".//td/text()""")[0]
            td_span = tr.xpath(""".//td/span/text()""")
            if len(td_span) == 0:
                td_span = ''
            else:
                td_span = td_span[0]
            data[td_f] = td_span
        self.table_key += 1
        self.db['tables'].insert_one(data)
        print(self.table_key)

    def test(self):
        url = 'https://gangkou.51240.com/BOSAN_3306__gk/'
        self.driver.get(url)
        source = self.driver.page_source
        html = etree.HTML(source)
        trs = html.xpath("""//table[@width="100%"]/tbody//tr""")
        data = {}
        for tr in trs:
            td_f = tr.xpath(""".//td/text()""")[0]
            td_span = tr.xpath(""".//td/span/text()""")
            if len(td_span) == 0:
                td_span = ''
            else:
                td_span = td_span[0]
            data[td_f] = td_span
        print(data)


if __name__ == "__main__":
    spider = LagouSpider()
    spider.run()
    # spider.test()
