import re

String = "人的知识愈广，人的本身也愈臻完善。人的知识愈广，人的本身也愈臻完善。"
# 匹配的字符串
p = re.compile("a")

# 被匹配字符串
print(p.match("a"))

# 单个元字符：. ^ $ * + ? {m} {m,n} [] |

# 正则表达式元字符：. 匹配单个字符,一个点就是一个字符，从索引为0开始
p1 = re.compile(".")
print(p1.match(String))

p2 = re.compile("人.知识")
print(p2.match(String))

# p2 = re.compile("....")  # 任意字符 出现4次
p2 = re.compile(".{4}")
print(p2.match(String))

# 正则表达式元字符：^ 以什么内容做开头，搜索和替换时很重要
p3 = re.compile("^人的知识愈广")
print(p3.match(String))

# 正则表达式元字符：$ 以什么内容做结尾，从后往前搜索，文件和路径处理时经常使用
p4 = re.compile("也愈臻完善。$")
print(p4.match(String))

# 正则表达式元字符：* 匹配前面的一个字符出现0次或多次
p5 = re.compile("ca*t")
print(p5.match("caaaat"))
print(p5.match("ct"))

# 正则表达式元字符：+ 前面的一个字符出现一次或多次
p6 = re.compile("ca+t")
print(p6.match("caaaat"))
print(p6.match("cat"))
print(p6.match("ct"))

# 正则表达式元字符：? 前面的一个字符出现0次或一次
p7 = re.compile("ca?t")
print(p7.match("caat"))  # 返回None
print(p7.match("cat"))
print(p7.match("ct"))

# 正则表达式元字符：{}
# 匹配字符”a“出现4次
p7 = re.compile("ca{4}t")
print(p7.match("caaaat"))
print(p7.match("caaat"))

# 匹配字符”a“出现4~6次
p7 = re.compile("ca{4,6}t")
print(p7.match("caaaat"))
print(p7.match("caaaaaat"))

# 正则表达式元字符：[] 匹配中间任意一个字符
p8 = re.compile("c[abc]t")
print(p8.match("cat"))
print(p8.match("cbt"))
print(p8.match("cdt"))

# 正则表达式元字符：| 或 通常和()结合使用


# 转译元字符：\d（表示匹配的时一串数字） \D（匹配不包含数字的） \s（表示匹配的是字符串） ()（分组）

# ^$ 表示空行

# .*? 不适用贪婪模式，只匹配第一个匹配到的内容
