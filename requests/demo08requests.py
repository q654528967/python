import requests
# responese = requests.get("https://www.baidu.com")
# print(type(responese.text))
# print(responese.text)
# print(type(responese.content))
# print(responese.content.decode('utf-8'))
# print(responese.url)
# print(responese.encoding)
# print(responese.status_code)
params = {
    'ie': 'utf-8',
    'f': 8,
    'rsv_bp': 1,
    'rsv_idx': 1,
    'tn': 'baidu',
    'wd': '中国'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36'
}
response = requests.get('https://www.baidu.com/s', params=params, headers=headers)
with open('testBaidu.html', 'w', encoding='utf-8') as fs:
    fs.write(response.content.decode('utf-8'))
print(response.url)


