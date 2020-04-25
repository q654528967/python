import re
import requests

url = 'https://www.gushiwen.org/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108'
                  ' Safari/537.36'
}
response = requests.get(url, headers=headers)
text = response.text
title = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
content = re.findall(r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)
for x in content:
    x = re.sub(r'<.*?>', '', x).strip()
    print(x)
