import requests
from lxml import etree
from urllib import request
import os
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36'
}


def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("""//div[@class='page-content text-center']//img[@class!='gif']""")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。!！\&\$\*\@\#\<]', '', alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        request.urlretrieve(img_url, 'images/'+filename)


def main():
    for x in range(1, 51):
        url = 'https://www.doutula.com/photo/list/?page=%s' % x
        parse_page(url)


if __name__ == '__main__':
    main()


