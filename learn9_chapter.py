"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习 9-章节
# author  : QLS
# time    : 2017/11/5 19:45
"""****************-*******************"""
from class_dog import Dog, Cat
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