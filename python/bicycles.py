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
