from urllib import request
from urllib import parse
# request.urlretrieve('http://www.baidu.com', 'baidu.html')
params = {'name': '张珊', 'age': 17, 'greet': 'hello world'}
result = parse.urlencode(params)
result2 = parse.parse_qs(result)
url = 'http://www.baidu.com/s?'
url2 = {'ie': 'UTF-8', 'wd': '刘德华'}
url2 = parse.urlencode(url2)
url = url + url2
print(url)
result3 = request.urlopen(url)
print(result3.read())


