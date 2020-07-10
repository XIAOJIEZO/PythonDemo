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

"""
练习：
1、使用for循环，打印数字1~20
2、创建一个列表，包含数字1~1000000，再使用for循环将这些数字打印出来
3、计算列表的最大值、最小值以及和
4、创建列表，包含1~20的奇数，再使用for循环将这些数字打印出来
5、创建一个列表，包含3~30能被3整除的数字，再使用for循环将这些数字打印出来
6、创建一个列表，其中包含1~10的立方，再使用for循环将这些数字打印出来
7、使用列表解析生成一个列表，其中包含1~10的立方
"""
# 1
for i in range(1, 21):
    print(i)

# 2
list_1 = []
#for i in range(1, 1000001):
#    list_1.append(i)        
list_1 = list(range(1, 1000001))    # 优化写法

for i in list_1:
    print(i)
    
# 3
print('min(list_1)=', min(list_1))
print('max(list_1)=', max(list_1))
print('sum(list_1)=', sum(list_1))

# 4
odd_numbers = []
for odd_number in range(1, 21, 2):
    odd_numbers.append(odd_number)

for odd_number in odd_numbers:
    print(odd_number)
    
# 5
multiple_3 = []
for num in range(3, 31, 3):
    multiple_3.append(num)

for num in multiple_3:
    print(num)
    
# 6
cube = []
for num in range(1, 11):
    cube.append(num**3)

for num in cube:
    print(num)
    
# 7
cube_1 = [num**3 for num in range(1, 11)]
print(cube_1)