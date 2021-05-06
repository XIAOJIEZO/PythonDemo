# 函数的迭代器与生成器
list = [1, 2, 3, 4]
for i in list:
    print(i)

# for循环就是一种迭代器，能够实现这种方法的的函数就是迭代器，每调用一次next()，就会输出iter当中的下一个元素
it = iter(list)
print(next(it))
print(next(it))


# 自己制作一个迭代器，称为生成器
# for i in range(10, 20, 0.5):  # 步长只能int
#     print(i)

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x  # 带yield的称为迭代器
        x += step


for i in frange(10, 20, 0.5):
    print(i)
