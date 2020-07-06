"""
python中的变量不需要声明，每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型
"""

counter = 100           # 整形变量
miles   = 1000.0        # 浮点型变量
name    = "Atrox"       # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1

a, b, c = 1, 2, 'Atrox'

"""
标准数据类型：Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Set（集合）、Dictionary（字典）
不可变数据：Number、String、Tuple
可变数据：List、Dictionary、Set
"""

"""
Number：int、float、bool、complex（复数）
type()函数查询数据类型，也可以用isinstance来判断
"""
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

e = isinstance(a, int); f = isinstance(a, bool)
print(e, f)


'''
数值运算，在混合计算时，整形会转换成浮点数
5 + 4    = 9   加法
4.3 - 2  = 4.3 减法
3 * 7    = 21  乘法
2 / 4    = 0.5 除法，得到一个浮点数
2 // 4   = 0   除法，得到一个整数
17 % 3   = 2   取余
2 ** 5   = 32  乘方
'''

"""
String
字符串截取：变量[头下标:尾下标]，包头不包尾
"""
str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串


"""
列表
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
"""

# 列表截取语法：变量[头下标:尾下标]
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表