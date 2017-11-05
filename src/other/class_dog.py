"""****************-*******************"""
# describe: 类练习
# author  : QLS
# time    : 2017/11/5 19:59
"""****************-*******************"""

class Dog(object):  # 更加约定，首字母大写的，被指定为类,python2.7要加object

    def __init__(self, name, age):  # 初始化类属性 name 和 age，默认类初始化__init__(self)
        self.name = name  # self.name 自己定义的， name 形参赋值
        self.age = age
        self.color = 'white'
    """
    类中的函数称为方法
    __init__()是一个特殊的方法，每当你根据Dog类创建实例时，python就会自动运行它，方法名称的开头和结尾的下划线
    为约定，旨在避免python默认方法和普通方法发生名称冲突
    方法定义中self必不可少，还必须放在其他形参的前面，为什么必须包含self？，因为python调用这个__init__()方法
    来创建Dog实例时，将自动传入实参self，每个与类关联的方法调用都自动传递实参self，他是一个指向实例本身的引用
    让实例能够访问类中的属性和方法，当我们创建DOg实例时，传入name和age，不用传入self，self自动传入
    以self为前缀的变量self.name都可供类中的所有方法使用，使用时self.name，相当于全局变量，
    通过实例访问的变量称为属性
    init可以指定属性默认值
        理解扩展，在init里面定义Dog类的属性值，并可以设置默认值，不设置默认值的的可以通过形参设置
    属性值修改
        1.实例修改，实例找到属性，并修改
        2.方法修改 self.属性 = x
        3.通过方法递增 self.属性 += x
        
    """

    def sit(self):  # 模拟小狗被命令蹲下，sit自己定义，self自动生成,类本身及属性
        print(self.name.title() + " is now sitting .")

    def roll_over(self):  # 模拟小狗打滚
        print(self.name.title() + "rolled over")

#  上面为类Dog范围


class Cat(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)
# 猫类

"""* 继承 *"""
class WhiteDog(Dog):  # Dog 称为超类superclass，
    def __init__(self, name, age):
        super().__init__(name, age)  # 继承父类用（父类）， __init__初始化父类，用super.__init__
# 继承父类 的所有属性和方法，在定义自己的
# 注意python2.7中，需要用super(WhiteDog, self).__init__(name, age)初始化父类
        self.sex = 'man'  # 给子类定义属性和方法
        self.similarCat = Cat("狗有点像猫", 100)  # 实例作属性时即创建了实例给这个属性
        # 记得初始化 __init__() missing 2 required positional arguments: 'name' and 'age'

    def run(self):
        print(self.name + "跑")

    def sit(self):  # 当子类的方法名和父类一样时，python将不会考虑这个父类的方法，即调用时先判断
        # 子类有没有这个方法，如果有，直接用，如果没有，则调用父类的，保留精华，去除糟粕
        print("这个狗笨，不会坐")

# my_dog = Dog("xiaobai", 2)  # 本文件中创建类实例
# print(my_dog.name)
# print(my_dog.color)
# my_dog.color = 'black'
# print(my_dog.color)

print("**************** Describe:注意java中方法不分顺序，但python分 *******************")

my_white_dog = WhiteDog("小黄", 12)
my_white_dog.sit()
my_white_dog.roll_over()
my_white_dog.run()
print(my_white_dog.sex)
my_white_dog.sit()

print("**************** Describe:实例作属性 *******************")
my_white_dog.similarCat.get_name()
print("活成精了，年龄都" + str(my_white_dog.similarCat.age) + "岁了")  # age是int记得用str

my_cat = Cat("xiaohei", 3)
print(my_cat.name)  # self.x 类属性，用实例.属性调用
my_cat.get_name()  # 类里面的方法用实例.方法名调用
print("**************** Describe:83 *******************")
"""
将一个独立的类的实例用作另一个类的属性，即这个属性包含了很多特性，可单独拿出来
类当属性时用 self.属性名 = 独立类 这个属性代表了一个类，
调用时 实例.属性名.具体的属性或者方法即（实例.属性名） = 另一个类的实例
"""
