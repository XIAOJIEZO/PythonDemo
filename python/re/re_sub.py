import re

# 替换内容re.sub(匹配规则,替换成什么内容,被匹配字符串)
String = "123-456-78901 # 这是电话号码"

# 删除所有非数字字符
p = re.sub(r"\D", "", String)
print(p)

# 去掉后面的注释
p2 = re.sub(r"#.*$", "", String)
print(p2)
