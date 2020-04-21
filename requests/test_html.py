from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('test1.html', parser=parser)
# trs = html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
# trs = html.xpath("//tr[2]")[0]
# print(etree.tostring(trs, encoding='utf-8').decode('utf-8'))

# trs = html.xpath('//tr[@class="event"]')
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
positions = []
trs = html.xpath("//tr[position()>1]")
for tr in trs:
    href = tr.xpath('.//a/@href')[1]
    title = tr.xpath('./td[2]/a/text()')[0]
    position = {
        "url": href,
        "title": title
    }
    positions.append(position)
print(positions)
