from urllib import request
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print(resp.read())

handle = request.ProxyHandler({'http': '175.161.14.134:9000'})
opener = request.build_opener(handle)
resp2 = opener.open(url)
print(resp2.read())
