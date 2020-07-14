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
print(1==1)     # true
print(1==2)     # false

# 检查是否不相等   !=
print(1!=1)     # FALSE
print(1!=2)     # true

# 比较数字
age = 18
if age == 20:
    print('小明的年龄是20岁！')
else:
    print('小明的年龄是', age, '岁！')

