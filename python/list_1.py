# 操作列表
# 遍历列表，使用for循环
legends = ['盖伦', '亚索', '劫', '艾瑞莉娅', '李青']
for name in legends:        # 循环遍历列表，将遍历到的值存储到变量name
    print(name)

# 创建数字列表：需要存储一组数字的原因有很多，例如，在游戏中，需要跟踪每个角色的位置，还需要跟踪玩家的几个最高的分。在数据的可视化中，处理的几乎都是由数字组成的集合

# 使用函数range()
for value in range(1, 5):
    print(value)        # 1 2 3 4 包头不包尾

# 使用range()创建数字列表
numbers = list(range(1, 6))     # 使用方法list()，将其转换为列表
print(numbers)

# 函数range()可以指定步长
even_numbers = list(range(1, 10, 3))    # 从1开始，每次值加3，到10结束(不包括10)
print(even_numbers)                     # [1, 4, 7]

# 创建一个列表，其中1~10的乘方
sqares = []
for i in range(1, 11):
    sqares.append(i**2)
print(sqares)

# 对列表进行简单的统计
digits = []
for i in range(0, 10):
    digits.append(i)
print(digits)
print('最大值为：', max(digits))
print('最小值为：', min(digits))
print('和为：', sum(digits))

# 列表解析，前面生成列表使用了三四行代码，列表解析只用一行代码就能生成这样的列表
digits_1 = [i**2 for i in range(0, 10)] # 首先指定一个列表名，指定一个左方括号，定义一个表达式（i**2）,用于生成储存到列表中的值，编写一个for循环，给表达式提供值，再加上右方括号
print(digits_1)