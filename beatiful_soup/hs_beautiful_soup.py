import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36'
}
url = 'https://www.hsbianma.com/'

respones = requests.get(url, headers=headers)
text = respones.content.decode('utf-8')
html = BeautifulSoup(text, 'lxml')
trs = html.find_all('tr')[1:]
hs_s = {}
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)
    # for info in infos:
    #     print(info)
    #     print('-'*30)
    break

