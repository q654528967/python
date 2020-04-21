from bs4 import BeautifulSoup
html = BeautifulSoup(open('hs.html', encoding='utf-8'), 'lxml')
trs = html.select('tr a')
for tr in trs:
    hr = tr['href']
    a_text = list(tr.strings)[0]
    print(a_text, type(a_text))
