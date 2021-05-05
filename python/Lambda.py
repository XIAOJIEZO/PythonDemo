def add(a, b):
    return a + b


add(3, 5)

# 省略函数名，省略return
def add(a, b): return a + b


# 简单的表达式可以使用表达式
f = lambda a, b: a + b
print(f(2, 3))
