from urllib import request, parse
from http.cookiejar import CookieJar
# 登录
# 1.1 创建一个CookieJar对象
cookiejar = CookieJar()
# 1.2 使用cookiejar创建一个HTTPCookieProcesso(cookiejar)
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 使用上一步创建的handler创建一个opener
opener = request.build_opener(handler)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36',
    'Referer': 'http://www.renren.com/416255995/newsfeed/photo'
}
data = {
    'email': '654528967@qq.com',
    'password': 'leiping123'
}
url = 'http://www.renren.com/PLogin.do'
req = request.Request(url=url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
opener.open(req)
# 访问个人主页
dapeng_url = 'http://www.renren.com/880151247/profile'
resp = opener.open(dapeng_url)
with open('dapeng.html', 'w', encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))
