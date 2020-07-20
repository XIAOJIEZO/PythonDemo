# 传递列表
def display_hello(names):
    for name in names:
        print('hello ' + name.title())


names = ['jack', 'logan', 'tony']
display_hello(names)

# 在函数中修改列表
# 将列表中的值打印后删除移动到另一个列表中,再打印出完整列表
def display_list1(list1, list2):
    """显示打印list1所有的值，将list1已打印的值转移的list2"""
    while list1:
        a = list1.pop()
        print('打印list1的值：' + str(a))
        list2.append(a)

def display_list2(list2):
    """打印list2所有值"""
    for i in list2:
        print(i)

list1 = [1, 'hello', 998, '周杰伦']
list2 = []

display_list1(list1, list2)     # 这一步list2的值已经被修改
display_list2(list2)

# 禁止函数修改列表：有时候我们需要保留原始的列表，此时可像函数传递此列表的副本
list1 = [1, 'hello', 998, '周杰伦']
list2 = []

display_list1(list1[:], list2)      # 使用切片传递列表副本
display_list2(list2)
print(list1)                        # 验证list1没有被改变

"""
练习：
1、创建一个包含魔术师的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字
2、在上一个练习的基础上，编写一个应为make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中加入字样“the Great“。调用函数show_magicians()，
    确认魔术师列表确实变了
3、在调用函数make_great()时，向他传递魔术师的列表的副本。返回修改后的列表，将其存储在另一个列表中。分别使用两个列表来调用show_magicians()函数，
    确认一个列表包含的是原来的列表，另一个添加了“the Great”字样
"""
# 1
magicians = ['刘谦', 'tony', 'rookie']
magicians_make = []

def show_magicians(magicians):
    """打印魔术师名字"""
    if magicians == []:
        print('magicians is null')
    else:
        for magician in magicians:
            print(magician)

# 2
def make_great(magicians, magicians_make):
    """修改魔术师列表，增加字样'the Great'"""
    while magicians:
        magician = magicians.pop()
        magicians_make.append('the Great' + magician)


make_great(magicians, magicians_make)
show_magicians(magicians_make)      # 查看magicians_make是否被修改
show_magicians(magicians)           # 察看magicians是否被修改

# 3
magicians = ['刘谦', 'tony', 'rookie']
magicians_make = []

make_great(magicians[:], magicians_make)
show_magicians(magicians_make)      # 查看magicians_make是否被修改
show_magicians(magicians)           # 察看magicians是否被修改

# 传递任意数量的实参：有时候你预先不知道函数需要传递多少个参数，下面的函数只能使用*toppings，不管提供多少实参，这个形参都将它们统统收入囊中
# 比如一万炒饭，他需要很多配料，但你无法确定顾客需要加哪些配料。
def make_rice(*toppings):       # 形参*toppings（可任意命名）中的星号让Python创建一个名为toppings的空元祖，并将收到的信息都封装都这个元组中
    """打印顾客点的所有配料"""
    print(toppings)      # ('米饭', '鸡蛋', '牛肉', '老干妈')

make_rice('米饭', '鸡蛋')
make_rice('米饭', '鸡蛋', '牛肉', '老干妈')

# 上述直接打印出来的是一个元组，使用循环来妥善处理它
def make_rice_1(*toppings):
    """打印顾客点的所有配料"""
    print('顾客点的配料是：')
    for topping in toppings:
        print('- ' + topping)

make_rice_1('米饭', '鸡蛋', '牛肉', '老干妈')

# 结合使用位置实参和任意数量实参：如果要让函数接收不同类型的实参，必须在函数定义中将接纳任意数量的实参的形参放在最后
# 例如前面的例子，炒饭的分量（大、中、小）还需要一个表示尺寸的实参，必须将该形参放在*toppings前面
def make_rice_2(size, *toppings):
    """概述要制作的炒饭"""
    print('制作' + size + '炒饭的配料是：')
    for topping in toppings:
        print('- ' + topping)

make_rice_2('小', '米饭', '鸡蛋')
make_rice_2('大', '米饭', '鸡蛋', '牛肉', '老干妈')

# 使用任意数量的关键字实参：有时候，需要接受任意数量的实参，但预先不知道传递给函数的回事什么样的信息。可将函数编写成能够接受任意数量的键-值对
# 比如调查用户信息，只知道会调查名和姓，其他的信息任意
def build_profile(fist, last, **user_info):
    """创建一个列表包含我们知道的有关用户信息"""
    profile = {}
    profile['first_name'] = fist
    profile['last_name'] = last
    for k, v in user_info.items():      # 将键-值对存储到profile
        profile[k] = v
    return profile

user_profile = build_profile('tony', 'stark', age = '18', city = '纽约')
print(user_profile)

"""
练习：
1、三明治：编写一个函数，它接受顾客要在三明治中添加一系列食材。这个函数只有一个形参，并打印一条消息，对顾客点的三明治进行概述。
    调用三次函数，每次提供不同数量的实参
2、汽车：编写一个函数，将一辆车的信息存储在字典中，这个函数总是接受制造商和型号，还可以接受任意关键字的实参。
    调用这个函数
"""
# 1
def make_Sandwich(*adds):
    """打印顾客添加三明治的材料"""
    print('顾客点的制作三明治材料是')
    for add in adds:
        print('- ' + add)

make_Sandwich('面包', '生菜')
make_Sandwich('面包', '生菜', '火腿')
make_Sandwich('面包', '生菜', '鸡蛋', '番茄酱')

# 2
def cars_info(manufacturer, model, **cars_info):
    """创建一个字典存储汽车信息"""
    cars = {}
    cars[manufacturer] = manufacturer
    cars[model] = model
    for k, v in cars_info.items():
        cars[k] = v
    return cars

cars_info = cars_info('雪佛兰', '大黄蜂', color = '黄色', speed = '400')
print(cars_info)        # {'雪佛兰': '雪佛兰', '大黄蜂': '大黄蜂', 'color': '黄色', 'speed': '400'}

