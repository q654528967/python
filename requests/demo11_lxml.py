from lxml import etree

text = '<div>' \
       '    <ul>' \
       '        <li>你好</li>' \
       '<li>python</li>' \
       '</ul>' \
       '</div>'


def parse_text():
    html = etree.HTML(text)
    print(etree.tostring(html, encoding="utf-8").decode('utf-8'))


def parse_file():
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse('testBaidu.html', parser=parser)
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    parse_file()



