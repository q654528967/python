import requests
url = 'http://httpbin.org/ip'
proxy = {
    'https': '60.184.173.236:808'
}
hearders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36'
}
response = requests.get(url, proxies=proxy)
print(response.text)
