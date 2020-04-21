from urllib import request
url = 'http://www.renren.com/880151247/profile'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149'
                  ' Safari/537.36',
    'Cookie': 'anonymid=k8p94rnejbe1ce; depovince=GW; _r01_=1; JSESSIONID=abcKA5h-xign4hvfzwsfx; ick_login=dedd8fc6-873'
              'd-4080-bc92-cec8c6bdb3bc; taihe_bi_sdk_uid=8392bf6647794295eb5542b711d46d9b; taihe_bi_sdk_session=2d8287'
              '829039fa40ad424320cfad5c8f; t=a3a6e6788a28abcc20c3ef32cb7447862; societyguester=a3a6e6788a28abcc20c3ef32'
              'cb7447862; id=974173882; xnsid=ada5257e; ver=7.0; loginfrom=null; jebe_key=16f95575-f649-4c6d-b1d4-7ef1f'
              '17ddf96%7Cc1456da5d958a01a46456926fdc93b15%7C1586224645672%7C1%7C1586224643083; jebe_key=16f95575-f649-4'
              'c6d-b1d4-7ef1f17ddf96%7Cc1456da5d958a01a46456926fdc93b15%7C1586224645672%7C1%7C1586224643086; wp_fold=0;'
              ' jebecookies=e9342346-0f8b-4ded-b373-e2ea7df6f04e|||||'
}
req = request.Request(url=url, headers=header)
resp = request.urlopen(req)

with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))

