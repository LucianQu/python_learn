"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习 9-章节
# author  : QLS
# time    : 2017/11/5 19:45
"""****************-*******************"""
from src.other.class_dog import Dog, Cat
from collections import OrderedDict  # 标准库练习--键值对
"""
开始语：
    面向对象编程是最有效的软件编写方法之一，在面向 对象编程中，你编写现实世界中的事物和情景的类，并基于这些类创建对象
    定义类时，定义大类，即对象都有的通用行为，基于类创建对象时，每个对象都自动具备这种通用行为，然后再赋予特殊行为
    
    根据类创建对象被称为实例化，实例化后能使用类的实例，并指定存在实例的内容，定义可对这些实例执行哪些操作，你将编写
    一些类来扩展既有类的功能，让相似的类能够高效地共享代码，你将把自己编写的类存储在模块中，并在自己的程序导入其他人
    写的类。
"""
my_dog = Dog('hei', 1)  # 当我导入类创建实例调用时，那个module的类的实例的方法也执行了

my_cat = Cat('bai', 2)
"""
类学习在class_dog.py模块实现
"""
"""
* Learn End ! 
* Time    : 2017/11/5 21:54
* Page    : 87
* Comment : 学了17页，中间包括吃饭和其他的，累了，晚会游戏，睡觉，今天都能学会，
            感触：学的过程中和java做对比，感觉python集合了c和java的特性
"""

"""
* Learn Start !
* Time : 2017/11/6 0006 20:10
* Page : 87
* Addr : 搞Android累了，学会python再回家
"""

# 导入类就像他在文件中定义一样
# 虽然同一个模块中的类之间应该存在某种相关性，但可以根据需要在一个模块中存储任意数量的类，
# from car import Car, ElectricCar  # 从一个模块中导入多个类，用逗号分隔
"""* 从模块导入类和从模块导入方法是一个道理 *"""

# 类分散到多个模块或在一个模块建不同类
"""
from car import Car
class ElectriCar(Car):  # 该类在electric_car模块中
    .....
    
from car import Car
from electric_car import ElectriCar
"""
"""
自定义工作流
    刚开始代码结构尽可能简单，在一个文件中完成所有工作，确定正常后再将类移到独立的模块中
"""

print("**************** Describe:Python标准库 *******************")
# 标准库中的任何函数和类都能使用，只需要import导入
# 模块collections中的一个类 --OrderedDict
# 字典让你能够将信息关联起来，但他们不记录你添加键值对的顺序，要创建字典记录键值对顺序，可使用
# 模块collections中的orderDict类，该实例和字典相同，但记录添加顺序
# 与标准库（内部模块）相呼应的还有外部模块


order_dict = OrderedDict()  # 创建实例
order_dict["name"] = "qulusheng"
order_dict["age"] = "28"
order_dict["sex"] = "man"
for key, value in order_dict.items():  # 遍历时以添加顺序进行遍历
    print(key.title() + " = " + value.title())

print("**************** Describe:类编码风格 *******************")
# 驼峰命名：将类名中的美哥单词的首字母大写，而不使用下划线，实例名和模块名都采用小写，并加下划线
# 类内部空行一个分隔函数，模块空行两个分隔类
# 标准库和编写的模块都需要导入时，先导入标准库，添加一个空行，导入自己的或者外部的模块
print("**************** Describe:文件和异常学习 *******************")
# 学习目的：学会处理文件来处理大量数据，以及错误处理，避免程序在面对意外情形时崩溃，学习异常
# 他们是python创建的特殊对象，管理程序运行时出现的错误，学习模块json，用来保存用户数据，避免程序
# 停止运行后丢失。

# 流程：读取文件--》分析或者修改文件中的信息以及重新设置格式并写入文件，浏览器显示内容
with open('pi_digits.txt') as files:  # file 自定义名字
    # with在不需要访问文件后将其关闭，with是由python来决定的
    # 也可以使用open（）和close（）组合,但在不恰当时间关闭文件时程序将出错
    contents = files.read()  # read读取文件，作为字符串存在contents中，
    # 读的内容末尾多了空行，原因：read（)到达末尾时返回一个空字符串，而显示这个空字符串就是空行，可使用rstrip()去除
    print(contents)
    print("**************** Describe:88 *******************")
    print(contents.rstrip())
    # [Errno 2] No such file or directory: 'pi_digits.txt' 文件放在file文件夹下，是否需要导入模块
    # 文件放在同一个文件夹下，即chapter可以，原因：没有向python提供路径

with open("E:\pythonproject\36\git_test\python_learn\file.wx_pi_digits.txt") as file_name:
    content1 = file_name.read()
    print(content1)
