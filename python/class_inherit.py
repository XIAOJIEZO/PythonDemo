"""
    继承：编写类时，并非总是要从空白开始。如果你编写的类时另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，他将获得另一个类的所有属性和方法；
原有的类称为父类，而新类称为子类。子类继承其父类的所有属性和方法，同时还可以定义自己的属性和方法。
"""

class Car():
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
        
    def fill_gas_tank(self):
        """描述汽车油箱容量"""
        print('汽车最大容量5L')

# 创建一个汽车子类，电动车
class ElectricCar(Car): # 创建子类时，父类必须包含在当前文件中，且位于子类前面。括号内包含父类名称。
    """电动车的独特之处"""

    def __init__(self, make, model, year):  # 子类的方法__init__()，创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法__init__()需要父类施以援手。
        """初始化父类属性"""
        super().__init__(make, model, year) # super()是一个特殊函数，帮助Python将父类和子类关联起来，这行代码让Python调用父类方法__init__(),让子类实例包含父类所有属性。父类也称为超类。

my_tesla = ElectricCar('tesla', 'model 3', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.odometer_reading = 100
my_tesla.read_odometer()
my_tesla.increment_odomete(100)
my_tesla.read_odometer()

# 给子类定义属性和方法
class ElectricCar1(Car):     # 创建子类时，父类必须包含在当前文件中，且位于子类前面。括号内包含父类名称。
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类属性
        再初始化子类特有属性
        """
        super().__init__(make, model, year)
        self.battery_size = 50

    def describe_battery(self):
        print('这辆车电瓶容量为' + str(self.battery_size))

my_first_tesla = ElectricCar1('tesla', 'model s', 2016)
my_first_tesla.describe_battery()

# 重写父类方法：对于父类的方法，只要它不符合子类模拟的实物行为，都可对其进行重写。
class ElectricCar2(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类属性
        再初始化子类特有属性
        """
        super().__init__(make, model, year)
        self.battery_size = 50
    """重写fill_gas_tank()方法，方法名与父类方法同名"""
    def fill_gas_tank(self):
        print('电动车没有油箱')

my_second_tesla = ElectricCar2('tesla', 'model 2', 2017)
my_second_tesla.fill_gas_tank()

"""
    将实例用作属性：使用代码模拟实物时，给类添加的细节越来越多，属性和方法清单以及文件都越来越长。在这种情况下，可以将类的一部分作为一个独立的类提取出来，
将大型类拆分成多个协同工作的小类。
"""
class Battery():
    """模拟汽车电瓶"""

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kwh battery')

class ElectricCar3(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        # 将实例用作属性


my_third_tesla = ElectricCar3('tesla', 'model 2', 2018)
my_third_tesla.battery.describe_battery()   # Python在实例my_third_tesla查找battery属性，并对存储在该属性的Battery实例调用方法describe_battery()