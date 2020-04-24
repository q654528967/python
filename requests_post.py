import requests
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86'
                  ' Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Accept': 'application/json, text/javascript, */*; q=0.01'
}
urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
s = requests.Session()
s.get(urls, headers=headers, timeout=3)
cookie = s.cookies
responer = s.post(url, data=data, headers=headers, cookies=cookie)
print(responer.json())
# with open('logou.txt', 'w', encoding='utf-8') as fy:
#     fy.write(responer.json())
