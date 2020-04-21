from bs4 import BeautifulSoup
import requests
from pyecharts.charts import Bar


weathers = []


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987'
                      '.149 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    divs = soup.find('div', class_='conMidtab')
    tables = divs.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for key, tr in enumerate(trs):
            tds = tr.find_all('td')
            if key == 0:
                tds = tds[1:]
            city_weather = {}
            td_city = tds[0]
            city = list(td_city.stripped_strings)[0]
            city_weather['city'] = city
            city_temp = tds[-2]
            min_temp = list(city_temp.stripped_strings)[0]
            city_weather['temp'] = int(min_temp)
            weathers.append(city_weather)


def main():
    urls = [
        'http://www.weather.com.cn/textFC/gat.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hb.shtml'
    ]
    for url in urls:
        parse_page(url)
    weathers.sort(key=lambda x: x['temp'])
    print(weathers[0:11])


if __name__ == '__main__':
    main()
