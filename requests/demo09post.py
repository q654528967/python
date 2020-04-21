import requests
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
refreUrl = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',

}
s = requests.Session()
cookie = s.get(refreUrl, headers=headers).cookies
print(cookie.get_dict())
respones = requests.post(url, data=data, headers=headers, cookies=cookie)
print(type(respones.json()))
print(respones.json())
print(respones.headers)
