from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36'
}
base_url = 'https://www.dytt8.net'


def data_init(url):
    """

    :param url: 网址
    :type url: 字符串
    :return: a的href属性加基础网址
    :rtype: 字符串
    """
    response_data = requests.get(url, headers=headers)
    text = response_data.content.decode(encoding='gbk', errors='ignore')
    html = etree.HTML(text)
    a_href = html.xpath('//div[@class="bd3r"]/div[@class="co_area2"]/div[2]/ul//table[1]//a/@href')
    href = map(lambda x: base_url+x, a_href)
    return href


def parse_detail_page(url):
    movie = {}
    response_detail = requests.get(url)
    text = response_detail.content.decode(encoding='gbk', errors='ignore')
    html = etree.HTML(text)
    title = html.xpath('//div[@class="title_all"]//font/text()')[0]
    movie['title'] = title
    zoom = html.xpath('//div[@id="Zoom"]')[0]
    infos = zoom.xpath('.//text()')
    for key, txt in enumerate(infos):
        if txt.startswith('◎年　　代'):
            movie['year'] = txt.replace('◎年　　代', '').strip()
        elif txt.startswith('◎类　　别'):
            movie['country'] = txt.replace('◎类　　别', '').strip()
        elif txt.startswith('◎主　　演'):
            ss = txt.replace('◎主　　演', '').strip()
            actors = [ss]
            for x in range(key+1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif txt.startswith('◎简　　介'):
            tt = ''
            for x in range(key+1, len(infos)):
                if infos[x].startswith('【下载地址】'):
                    break
                tt += infos[x].strip()
            movie['detail'] = tt
            print(movie)


def get_dianyin():
    tst_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for i in range(1, 8):
        url = tst_url.format(i)
        detail_urls = data_init(url)
        for item in detail_urls:
            parse_detail_page(item)
            break
        break


if __name__ == '__main__':
    get_dianyin()

