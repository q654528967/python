from urllib import request, parse
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 ',
    'Referer': 'https://www.lagou.com/jobs/list_python/p-city_3?&cl=false&fromSearch=true&labelWords=&suginput='
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data, method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
