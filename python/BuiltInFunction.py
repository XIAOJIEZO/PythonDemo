from functools import reduce

# python内建函数
# filter： filter(function or None, iterable) --> filter object，把满足function条件的items取出来
a = [1, 2, 3, 4, 5, 6, 7]

print(list(filter(lambda x: x >= 4, a)))  # 返回的是filter对象，要强制转化成list

# map:多个参数进行依次处理
b = [2, 5, 6, 2]
c = [2, 5, 8, 7]

print(list(map(lambda x: x, b)))

# 实现相加
print(list(map(lambda x, y: x + y, b, c)))

# reduce：初始值与列表内上一个参数执行函数表达式，接着作为一个参数和后面的参数执行函数表达式（2+4+5+4...）
d = [4, 5, 4, 55, 5, 4]
print(reduce(lambda x, y: x + y, d, 2))
