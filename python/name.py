"""
变量的命名和使用:
1、只能包含字母、数字和下划线
2、变量名不能包含空格，使用下划线分割单词
3、不要使用Python关键字和函数名用作变量名
4、变量名应既简短又具有描述性
"""

"""
字符串：字符串就是一系列字符，用引号括起的就是字符，可以是单引号，也可以是双引号，这种灵活可以在字符串中包含引号
"""
message = '去吧："皮卡丘"'
print(message)

# 使用方法修改字符串大小写
name = 'roger J'
print(name.title())     # 首字母大写
print(name.upper())     # 全部转换为大写
print(name.lower())     # 全部转换为小写

# 拼接字符串:使用（+）来合并字符串
first_name = 'roger'
last_name = 'J'
full_name = first_name+' '+last_name
print('full_name=', full_name)

# 制表符&换行符添加空白
print('\tPython')   # 在输出前添加一个Tab长度
print('Language:\n\tPython\n\tJava')    # \n换行符