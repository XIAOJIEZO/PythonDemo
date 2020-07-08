"""
列表
1、列表由一系列按特定顺序的元素组合,列表是有序集合
2、可以将任何东西加入列表中，元素之间没有任何关系
"""
bicycles = ['hello', 'mobol', 'trek']
print(bicycles)

# 访问列表元素#、索引从0开始
print(bicycles[0])
print(bicycles[0].title())

# 从右往左，索引从-1开始
print(bicycles[-1])

# 使用列表中的各个值
message = '我的第一辆单车是' + bicycles[0].title() + '单车'
print(message)

# 修改元素
legend = ['亚索', '劫', 1, '菲兹']
print(legend)

legend[0] = "亚托克斯"      # 通过索引修改列表的元素
print(legend)

# 添加元素
legend.append('小鱼人')      # 加在列表末尾
print(legend)

lists = []   # 创建空列表
lists.append(1)
lists.append(2)

# 添加元素，使用insert()方法
legend.insert(0, 'akali')       # 在索引位置插入元素，既有的每个元素都右移一个位置
print(legend)

# 使用方法del()删除元素，可以删除任何位置元素，条件是知道索引，删除后的元素无法访问
del legend[0]
print(legend)

# 使用方法pop删除元素：将元素从列表中删除，并接着使用它的值，pop()可删除列表末尾的元素，并让你能够接着使用它
legends = ['亚索', '劫', 1, '菲兹']
print(legends)

pop_legends = legends.pop()     # 菲兹
print(legends)                  # 菲兹
print('pop_lengds=', pop_legends)

# 弹出列表中任何位置元素，使用方法pop()也可以删除任何位置元素，只需要知道索引
legends_1 = ['亚索', '劫', 1, '菲兹']
first_pop = legends_1.pop(0)
print('弹出第一个元素后的列表=', legends_1, '弹出的第一个数为：', first_pop)

# 根据值删除元素,还要方法remove()
legends_2 = ['yasuo', 'yasuo', 'akali', 'atrox']
legends_2.remove('yasuo')       # 只能移除第一个出现的值
print('legends_2 remove yasuo=', legends_2)

"""
练习：
1、邀请三个人共进晚餐
2、修改嘉宾名单，有人无法出席，重新邀请一位
3、找到更大的桌子，再邀请三位
4、餐桌没了
"""
guests = ['李白', '杜甫', '贺知章']
print('第一次邀请的人员名单为：', guests[0], guests[1], guests[2])

print('贺知章无法赴约，将其替换为“李清照”')
guests.remove('贺知章')
guests.append('李清照')
print('第二次邀请的人员名单为：', guests[0], guests[1], guests[2])

print('找到更大的桌子，再邀请三位')
guests.insert(0, '范仲淹')
guests.insert(3, '张楚岚')
guests.append('冯宝宝')
print('第三次邀请的人员名单为：', guests[0], guests[1], guests[2], guests[3], guests[4], guests[5])

print('餐桌没了，只能邀请两位了')
while len(guests) > 2:
    guests.pop()
    print('sorry', guests[len(guests)-1])

while len(guests) > 0:
    guest_1 = guests.pop()
    print('共进晚餐吧', guest_1)

print(guests)