from bs4 import BeautifulSoup
import requests

url = 'https://www.hsbianma.com/search?keywords=94'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108'
                  ' Safari/537.36'
}
text = requests.get(url, headers=headers)
html = text.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

trs = soup.find_all('tr')[1:][0]

# for tr in trs:
#     tds = tr.find_all('td')
#     title = tds[1].string
#     print(title)
# trs = soup.find_all('tr', limit=2)[1]
# trs = soup.find_all('tr', class_='result-grid')
# trs = soup.find_all('tr', attrs={
#     'class': 'result-grid'
# })
# print(trs)
# input_list = soup.find_all('input', id='keywords', class_='key_in')
# print(input_list, end='-'*30)
# input_list2 = soup.find_all('input', attrs={
#     'id': 'keywords',
#     'name': 'keywords'
# })
# print(input_list2, type(input_list2))
# hrefs = soup.find_all('a')
# for hrefE in hrefs:
#     link = hrefE['href']
#     li = hrefE.attrs['href']
#     print(link, type(link))
#     print(li, type(li))
# print(trs)
# for tr in trs:
#     print(tr, type(tr), end='-'*30)
#     break

