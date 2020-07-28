"""
    使用类和实例：你可以使用类来模拟现实中的很多情景。类编写好后，你的大部分时间都将花在使用根据类创建的实例上。你需要执行一个重要的任务是修改实例的属性。
你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。
"""

# 下面编写一个表示汽车的类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())

"""
    给属性指定默认值：类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__()内指定之中初始值是可行的；
如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
"""
class Car1():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      # 默认值

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('这辆汽车的里程是' + str(self.odometer_reading) + '公里')

    def updata_odometer(self, mileage):     # 方法里面的形参只能自己使用
        """修改里程数的值"""
        """我们还能在这个方法里面做很多操作，例如禁止里程往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('里程数不能忘回调')

    def increment_odomete(self, mileage):
        """里程数递增"""
        self.odometer_reading += mileage

my_car1 = Car1('audi', 'a4', 2016)
my_car1.read_odometer()

# 修改属性值：直接修改属性值、通过方法修改属性值
# 1、直接修改属性值
my_car1.odometer_reading = 99   # 通过访问属性修改属性值
my_car1.read_odometer()

# 2、通过方法修改属性值
my_car1.updata_odometer(1009)     # 调用updata_odometer方法
my_car1.read_odometer()

my_car1.updata_odometer(998)     # 里程数<1009
my_car1.read_odometer()

# 通过方法对属性值进行递增：有时候需要将属性值递增特定量，而不是将其设置为全新的值
my_car1.increment_odomete(100)
my_car1.read_odometer()

my_car1.increment_odomete(100)
my_car1.read_odometer()
