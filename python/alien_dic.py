# 一个简单的字典
aline_0 ={'color': 'green', 'points': 5}
print(aline_0['color'])
print(aline_0['points'])

# 在Python中，字典是一系列键-值对，每个键都与一个值关联，可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表、乃至字典。
# 事实上，可将任何Python对象用作字典的值

# 访问字典中的值
# 如果玩家射杀了这个外星人，可以使用代码来确定玩家应获得多少点
new_points = aline_0['points']
print('你获得' + str(new_points) + '积分')   # 函数str()将整数转换为字符串

# 添加键-值对
# 添加外星人坐标
aline_0['x_position'] = 0
aline_0['y_position'] = 25
print(aline_0)

# 创建空字典
aline_1 = {}
print(aline_1)

# 修改字典中的值
# 将外星人的颜色改为yellow
print("这个外星人的颜色是" + aline_0['color'] + "。")

aline_0['color'] = 'yellow'
print("这个外星人的颜色是" + aline_0['color'] + "。")

# 删除键-值对：对于字典中不在需要的信息，可使用del语句将键值对永久删除。使用del语句时，必须使用字典名和要删除的键
aline_1 = {'color': 'red'}
print(aline_1)

del aline_1['color']
print(aline_1)

'''
由类似对象组成的字典
    在前面的实例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也可以使用字典来存储总多对象的同一种信息。
    假设你调查很多人喜欢的的编程语言是什么，可以使用一个字典来存储这种简单调查的结果
'''
favorite_laguages = {
    'jen': 'python',
    'sarah': 'C'
}

"""
练习：
1、人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄、居住城市，将字典中的各项信息都打印出来
2、喜欢的数字：使用一个字典来存储一些人喜欢的数字。打印出每个人喜欢的数字。让程序更有趣，通过询问好友确保数据是真实的
"""
friend = {'first_name': '张', 'last_name': '楚岚', 'age': '22', 'city': '四川'}
for i in friend:
    print(i + '=' + str(friend[i]))

favorite_nums = {
    '张楚岚': 1,
    '冯宝宝': 2,
    '王也': 5,
    '诸葛青': 3
}
for name in favorite_nums:
    print(name + '喜欢的数字是' + str(favorite_nums[name]))
