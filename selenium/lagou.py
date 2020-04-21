from selenium import webdriver
from lxml import etree


class LagouSpider(object):
    driver_path = r'E:\chromedriver_win32\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=LagouSpider.driver_path
        )
        self.url = 'https://gangkou.51240.com/BOSAN_3306__gk/'

    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
        self.parse_list_page(source)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("""//table[@width='100%']//tr/td/text()""")
        for link in links:
            print(link)
        values = html.xpath("""////table[@width='100%']//tr/td/span/text()""")
        for value in values:
            print(value, type(value))
        self.driver.close()


if __name__ == "__main__":
    spider = LagouSpider()
    spider.run()
