# 导入整个模块：导入后可以调用该模块内的任意函数
import make_pizza

# 调用函数：模块名.函数名
make_pizza.make_pizza(16, '生菜')
make_pizza.make_pizza(20, '鸡蛋', '面粉')

# 导入特定函数
from make_pizza import make_pizza

# 调用函数：直接使用函数名
make_pizza(32, '牛肉', '生菜')

# 使用as给函数指定别名：如果要导入的函数名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名，类似于外号
from make_pizza import make_pizza as mp     # 将函数make_pizza()命名为mp()
mp(11, '牛肉', '生菜', '番茄')

# 导入模块中的所有函数：不是自己编写的大型模块时，不建议使用这种方法，可能会遇到多个名称相同的函数或变量
from make_pizza import *