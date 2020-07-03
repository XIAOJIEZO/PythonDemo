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

# Number：int、float、bool、complex（复数）
# type()函数查询数据类型，也可以用isinstance来判断
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

e = isinstance(a, int); f = isinstance(a, bool)
print(e, f)