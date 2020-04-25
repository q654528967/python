import re
# text = 'hello'
# ret = re.search('^h', text)
# print(ret.group())
# email = '654528967@qq.com'
# ret1 = re.search('\w+@[a-z]+.com$', email)
# print(ret1.group())
# url = 'httpsf'
# ret = re.match('(ftp|http|https)$', url)
# print(ret.group())
# text = '<h1>test</h1><h2>hh</h2>'
# ret = re.match('<.+?>', text)
# print(ret.group())
# num = '10110'
# ret = re.match('[1-9]\d?$|100$', num)
# print(ret.group())
text = "apple's price $99,orange's price is $10"
# ret = re.search('.*\$\d+.*\$\d+', text)
# print(ret.group())
# ret = re.findall('\$\d+', text)
# print(ret)
# ret = re.sub('\$\d+', '0', text)
# print(ret)
r = re.compile(r"""
\$+ #$本身
\d* #$后面的数字
""", re.VERBOSE)
ret = re.findall(r, text)
print(ret)
