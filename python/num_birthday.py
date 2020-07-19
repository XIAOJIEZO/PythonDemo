"""
数字:
1、整数
2、浮点数：Python将带小数点的数字都称为浮点数
"""

# 结果包含的小数位数可能是不确定的
num = 0.2 + 0.1     # 0.30000000000000004
num2 = 3 * 0.1      # 0.30000000000000004

# 使用函数str()避免类型错误
age = 23
# message = "Happy" + age + "rd Birthday"   不太类型拼接，报错
message = "Happy " + str(age) + "rd Birthday"
print(message)