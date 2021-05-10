import re

# 匹配出日期年月日
String = "2021-05-09"
p1 = re.compile("....-..-..")  # 此方法不可取，匹配格式可能不唯一2021-5-9
print(p1.match(String))


p2 = re.compile(r"(\d+)-(\d+)-(\d+)")
print(p2.match(String))
print("year:%s" % (p2.match(String).group(1)))
print("month:%s" % (p2.match(String).group(1)))
print("day:%s" % (p2.match(String).group(1)))
print(p2.match(String).groups())    # 返回tuple

# match匹配的字符串和正则必须是一一匹配的，如下就无法匹配，此时就需要search匹配
print(p2.match("aaa2021-05-09"))