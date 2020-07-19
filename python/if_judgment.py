# if语句
# 一个简单示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
# 条件测试：每条if语句的核心都是一个值未True或False的表达式，这种表达式被称为条件测试

# 检查是否相等  ==
print(1 == 1)     # true
print(1 == 2)     # false

# 检查是否不相等   !=
print(1 !=1 )     # FALSE
print(1 != 2)     # true

# 比较数字:== > < >= <= !=
age = 18
if age == 20:
    print('小明的年龄是20岁！')
else:
    print('小明的年龄是', age, '岁！')

# 检查多个条件，使用关键字 and 和 or
# 检查a，b是否都不小于10
a = 11
b = 9
if a > 10 and b > 10:
    print('a，b都大于10')
else:
    print('a，b不是都大于10')
    
# 检查a，b是否存在大于10
if a > 10 or b > 10:
    print('a，b存在大于10')
else:
    print('a，b不是都大于10')
    
# 检查特定值是否包含在特定列表中  in和not in
legends = ['盖伦', '亚索', '劫', '艾瑞莉娅', '李青']
legend = input('请输入英雄名称：')
if legend in legends:
    print(legend, '在列表内')
else:
    print(legend, '不在列表内')
    
# 布尔表达式：布尔表达式只有两种结果（True和False），判断语句后面跟的就是布尔表达式（True，False，1=2，1>3，legend in legends等）

# 测试多个条件；if-elif-else，通常情况下else可省略

"""
1、假设在游戏中射杀了一个外星人，创建变量alien_color，将其设置为green、yellow、red
2、检查外星人是否是绿色，如果是，打印信息提示玩家获得了5个点
3、编写两个版本，在第一个版本通过了，第二个版本未通过
"""
# 1
alien_color = {'alien1':'green', 'alien2':'yellow', 'alien3':'red'}

# 2
name = input('请输入外星人名字：')
if name in alien_color.keys():
    if alien_color[name] == 'green':
        print(name, '是绿色，获得五个积分')
    elif alien_color[name] == 'yellow':
        print(name, '是黄色，获得十个积分')
    else:
        print(name, '是红色，获得十五个积分')
else:
    print('输入的外星人名字不存在')
    
# 使用if语句处理列表
# 确定列表是不是空的
cars = []
if cars:                # cars为空，布尔表达式为False
    for car in cars:
        print(car)
else:
    print('cars is null')
    
cars = ['bmw']
if cars:                # cars不为空，布尔表达式为True
    for car in cars:
        print(car)
else:
    print('cars is null')
    
# 使用多个列表：判断legens_1的值是否在legends_2
legends_1 = ['盖伦', '亚索', '劫', '艾瑞莉娅', '李青']
legends_2 = ['盖伦', '亚索', '拉克丝', '艾瑞莉娅', '伊泽瑞尔']
for legend in legends_1:
    if legend in legends_2:
        print(legend, 'in legends_2')
    else:
        print(legend, 'not in legends_2')
        
"""
练习：
1、创建一个用户列表，包含admin、遍历列表向每个用户打印问候信息
    1.1 如果用户是admin，打印特殊的问候信息。”Hello admin,would you like to see a status report“
    1.2 否则，打印一条普通问候信息，”hello Jack,thank you for logging in again“
2、在上述的基础上，检查用户列表是否为空
    2.1 为空，打印”We need to find some users“
    2.2 删除列表中的所有用户，确定将打印正确的信息
"""
users = ['Jack', 'Eric', 'Logen', 'admin', 'Atrox']
for user in users:
    if user == 'admin':
        print('Hello admin,would you like to see a status report')
    else:
        print('hello', user, ',thank you for logging in again')
        
users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin,would you like to see a status report')
        else:
            print('hello', user, ',thank you for logging in again')
else:
    print('We need to find some users')
        
"""
2、模拟网站保证用户名都是独一无二的
    2.1 创建列表current_users
    2.2 创建列表new_users，保证有用户包含在current_users
    2.3 遍历new_users，检查每个用户是否被使用。如果被使用，指出需要使用别的用户名，否则指出这个用户未被使用
    2.4 确保比较时不区分大小写
"""
current_users = ['Jack', 'Eric', 'Logen', 'admin', 'Atrox']
current_users_upp = [user.upper() for user in current_users]
new_users = ['yasuo', 'eric', 'Zed', 'Roger', 'Atrox']
for user in new_users:
    if user.upper() in current_users_upp:
        print(user, '用户已存在')
    else:
        print('此用户未被使用')
