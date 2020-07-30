# 为了让文件尽可能整洁，将类存储在模块中，然后在主程序中导入所需的模块
from car import Car

my_new_car = Car('雪佛兰', '大黄蜂', 2016)
print(my_new_car.get_descriptive_name())

# 从一个模块中导入多个模块：from car import Car, ElectricCar

# 导入整个模块：import car

# 导入模块中所有类：from module_name import *

# 在一个模块中导入另一个模块