import time


# 闭包
def func():
    num1 = 1
    num2 = 2

    return num1 + num2  # 返回的是int


# 外部函数的变量被内部函数引用的方式，称为闭包
def sum(a):  # 外部函数
    def add(b):  # 内部函数
        return a + b

    return add  # 返回的是function


# add 函数名称或函数的引用
# add() 函数的调用

num1 = sum(1)
print(num1(2))


# 计算函数y = a*x + b
def a_line(a, b):
    def arg_y(x):
        return a * x + b

    return arg_y


# a=3, b=4, x=5
line = a_line(3, 4)
y = line(5)
print("a*x + b = " + str(y))


# 优化写法
def b_line(a, b):
    return lambda x: a * x + b


# 定义装饰器，计算程序运行时间
def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        print("运行程序所花时间为" + str(time.time() - start_time) + "s")

    return wrapper


@timmer
def time_sleep():
    time.sleep(3)


time_sleep()


# 给装饰器传参，带参数的函数处理
def new_tips(argv):
    def tips(func):
        def wrapper(a, b):
            print("start \n"
                  "argv：%s \n "
                  "funcname:%s" % (argv, func.__name__))
            func(a, b)
            print("stop")

        return wrapper

    return tips


@new_tips("tips1")
def add(a, b):
    print("a+b=%d" % (a + b))


add(5, 77)

# 自定义上下文管理器
fd = open("name.txt")
try:
    for line in fd:
        print(line)
finally:
    fd.closed()

# 使用with就不需要使用finally了
with open("name.txt") as f:
    for line in fd:
        print(line)