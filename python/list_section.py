# 使用列表的一部分
# 切片：要创建切片，可指定要使用的第一个元素与最后一个元素的索引
legends = ['盖伦', '亚索', '劫', '艾瑞莉娅', '李青']
print(legends[1:4])    # 切片，输出第2~4位置元素
print(legends[:4])     # 没有指定第一个索引，从头开始
print(legends[1:])     # 没有指定结尾，一直到结束

# 遍历切片：想要遍历列表的部分元素，可在for循环中使用切片
# 遍历前三位，并打印他们的名字
for name in legends[:3]:
    print(name)

# 通常情况下，切片很有用。例如，编写游戏时，你可以在玩家退出游戏时将其最终得分加入到一个列表中。然后，为获取玩家的三个最高得分，你可以将列表降序排序，在创建一个只包含前三得分的切片

# 复制列表
# 要复制列表，可创建一个包含整个列表的切片，方法是省略起始索引和终止索引（[:]）
legends_1 = ['盖伦', '亚索', '劫', '艾瑞莉娅', '李青']
legends_2 = legends_1[:]
print('legends_1=', legends_1)
print('legends_2=', legends_2)

# legends_2添加一个元素，验证legends_1有没有改变
legends_2.append('索尔')
print('legends_1=', legends_1)
print('legends_2=', legends_2)

# 将legends_3赋值给legends_4，实际上将新变量legends_4关联到包含在legends_3中的列表，因此这两个变量都指向同一个列表，当列表元素发生改变，两个变量同时改变
legends_3 = ['盖伦', '亚索', '劫', '艾瑞莉娅', '李青']
legends_4 = legends_3
print('legends_3=', legends_3)
print('legends_4=', legends_4)

legends_3.append('卢锡安')
print('legends_3=', legends_3)
print('legends_4=', legends_4)