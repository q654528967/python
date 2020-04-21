import requests
from bs4 import BeautifulSoup

url = 'https://gangkou.51240.com/BOSAN_3306__gk/'
text = requests.get(url).content.decode('utf-8')
print(text)
soup = BeautifulSoup(text, 'lxml')
trs = soup.select('#fcj_jg table tr')
result = {}
for tr in trs:
    print(tr, end='tr\n')
    res = list(tr.stripped_strings)
    print(res, end='list_tr\n')
    if len(res) == 2:
        result[res[0]] = res[1]
    else:
        result[res[0]] = ''
print(result, end='res\n')

