class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 默认值

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('这辆汽车的里程是' + str(self.odometer_reading) + '公里')

    def updata_odometer(self, mileage):  # 方法里面的形参只能自己使用
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
