# input()函数
name = input('请输入你的姓名：')        # 输入的是字符串
print(type(name))   # <class 'str'>

age = int(input('请输入你的年龄：'))    # 有时候需要转换其数据类型
print(type(age))    # <class 'int'>

# 求模运算符：%（求余数），可以用这一点来判断一个数是奇数还是偶数
num = intinput('请输入一个正整数：')
num = int(num)
if num % 2 == 0:
    print(str(num) + '是整数')
else:
    print(str(num) + '是奇数')