from urllib import parse
url = 'https://www.baidu.com/s?wd=python&username=abc#1'
result = parse.urlparse(url)
result2 = parse.urlsplit(url)
print(result)
print(result2)
print('scheme:', result.scheme)
print('netloc:', result.netloc)
print('path:', result.path)
print('params:', result.params)
print('query:', result.query)
print('fragment:', result.fragment)

