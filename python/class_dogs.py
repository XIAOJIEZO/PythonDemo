"""
面向对象编程是最有效的软件 编写方法之一。
创建和使用类：使用类几乎可以模拟任何东西。下面编写一个表示小狗的简单类Dog，对于宠物狗，我们知道他们有名字、年龄；我们还知道小狗还会蹲下和打滚。
"""


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模仿小狗被命令是蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模仿小狗被命令式打滚"""
        print(self.name.title() + " rolled over!")


"""
方法__init__()
    类中的函数成为方法：__init__()是一种特殊的方法，每当你根据Dog类创建新实例时，Python会自动运行它。开头和末尾各有两个下划线，这是一种约定，
旨在避免Python默认方法与普通方法发生名称冲突。
    三个参数：self、name、age。在这个方法的定义中，形参self必不可少、还必须位于其他形参前面。为何必须在方法定义中包含self？因为Python调用__init__()
方法来创建Dog实例时、将自动传入实参self。
    每个与类相关联的方法调用都自动传递实参self，他是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    定义两个变量都有前缀self。以self为前缀的变量都可提供类中所有方法使用，我们还可以通过类的任何实例来访问这些变量。self.name = name获取存储在
形参name中的值，并将其存储在变量name中，然后该变量被关联到当前创建的实例。

Dog类还定义了另外两个方法：由于这些方法不需要额外的信息，因此他们只有一个形参self。
"""

# 根据类创建实例
my_dog = Dog('urf', 3)  # 创建一个实例

print('My dog name is' + my_dog.name.title() + '.')  # 访问属性 实例名.属性
print('My dog is ' + str(my_dog.age) + ' years old.')

# 调用方法
my_dog.sit()  # 实例名.方法名
my_dog.roll_over()

# 创建多个实例：每条小狗都是一天独立的实例，有自己的一组属性，能够执行相同的操作
your_dog = Dog('lucy', 4)
his_dog = Dog('willie', 2)

"""
练习
    1、餐馆：创建一个名为Restaurant的类，其方法__init__()中设置两个属性：restaurant_name和cuisine_type。创建一个describe_restaurant()
的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条信息，指出餐馆正在营业。
    创建一个实例，打印两个属性，调用两个方法。
    
    2、三家餐馆：创建三个实例，调用describe_restaurant()方法
    
    3、用户：创建一个User类，其中包含first_name和last_name，还要用户简介通常会储存的其他几个属性。定义方法describe_user()的方法，打印用户
信息摘要；再定义一个greet_user()方法，向用户发出个性化问候。
    创建多个实例
"""


# 1
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + '是一个' + self.cuisine_type + '类型的餐馆。')

    def open_restaurant(self):
        print(self.restaurant_name + '餐厅现在正在营业！')


restaurant = Restaurant('川味道', '川菜')
print('restaurant_name = ' + restaurant.restaurant_name)
print('cuisine_type = ' + restaurant.cuisine_type)
restaurant.open_restaurant()


# 3
class User():

    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def describe_user(self):
        print(self.first_name + self.last_name + ',' + str(self.age) + '岁' + self.sex + '性！')

    def greet_user(self):
        print('你好,' + self.first_name + self.last_name + '!')


zcl = User('张', '楚岚', '男', 18)
fbb = User('冯', '宝宝', '女', 100)

zcl.describe_user()
zcl.greet_user()

fbb.describe_user()
fbb.greet_user()


# 属性添加"__"外部无法直接访问到，只能通过方法来修改私有属性
class Player():
    def __init__(self, name, hp, occu):
        self.__name = name
        self.hp = hp
        self.occu = occu

    def newname(self, newname):
        self.__name = newname

    def show(self):
        Str = self.__name + "：" + self.hp + " " + self.occu
        print(Str)


player = Player("阿七", "100", "刺客")
player.show()
player.hp = "90"
player.newname("大宝")
player.show()
