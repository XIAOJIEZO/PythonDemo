"""
将函数存储在模块中:函数的优点之一是，使用它们可将代码与主程序分离。通过给函数指定描述性的名称，可让主程序容易理解得多。
你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。
"""
# 定义一个函数，在def_import.py文件中调用这个函数
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print('制作' + str(size) + '号pizza的材料是：')
    for topping in toppings:
        print('- ' + topping)

