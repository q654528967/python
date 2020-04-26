import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36',
    'Referer': 'https://www.kuaidi100.com/global/ups.shtml?from=openv'
}
text = '1Z7WE3150346530901'
url = 'https://www.kuaidi100.com/query?type=ups&postid=%s&id=1&valicode=&temp=0.8200502115817585&phone=' \
      '' % text


response = requests.get(url, headers=headers)

text = response.text

print(text)


