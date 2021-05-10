import re

# search经常用于搜索指定字符串

with open("../files/TheMostBeautifulEncounter", mode='r', encoding="utf8") as f:
    content = f.read()
    print(content)

    p = re.search("前世五百年的回眸", content)
    print(p)
    p = re.compile("我")

    print(p.match(content))

    # match和search只匹配第一个字符串
    # 无括号匹配整体，有括号匹配括号内内容
    p = re.findall("前世五.*?百年的回眸", content)  # ['前世五百年的回眸', '前世五六七百年的回眸', '前世五六百年的回眸']
    print(p)

    p = re.findall("前世五.+?百年的回眸", content)  # ['前世五六七百年的回眸', '前世五六百年的回眸']
    print(p)

    p = re.findall("前世五(.*?)百年的回眸", content)    # ['', '六七', '六']
    print(p)

    p = re.findall("前世五(.+?)百年的回眸", content)  # ['六七', '六']
    print(p)
