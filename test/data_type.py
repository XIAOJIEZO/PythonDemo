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







"""
Tuple：元组与列表类似，元组的元素不能改变，元组写在小括号里，元素之间用逗号隔开，元素类型可以不相同
"""
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置
tup = (1, 2, 3, 4, 5, 6)
print('tup[0]=', tup[0])
print('tup[1:5]=', tup[1:5])

# 修改元组元素的操作是非法的 tup[0] = 11
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则
# tup1 = ()    空元组
# tup2 = (20,) 一个元素，需要在元素后添加逗号

"""
set:集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print('集合a=', a)
print('集合b=', b)
print('a和b的差集=', a - b)     # a 和 b 的差集

print('a和b的并集=', a | b)     # a 和 b 的并集

print('a和b的交集=', a & b)     # a 和 b 的交集

print('a和b中不同时存在的元素=', a ^ b)     # a 和 b 中不同时存在的元素















