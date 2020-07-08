print("hello python world")

# 第一个注释
print('hello ,python!')

# \ 转义符  r去掉转义
print('转义,\n换行')
print(r'转义,\n换行')

# 等待用户输入
a = input('请输入，按回车结束：')
print('你输入的内容是：'+a)

# print输出默认换行，变量末尾加 end=""不换行
x = "a"
y = "b"
print(x)
print(y)

print(x, end="")
print(y)

"""
变量的命名和使用:
1、只能包含字母、数字和下划线
2、变量名不能包含空格，使用下划线分割单词
3、不要使用Python关键字和函数名用作变量名
4、变量名应既简短又具有描述性
"""
