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
# with open('pi.txt') as files:  # file 自定义名字
#     # with在不需要访问文件后将其关闭，with是由python来决定的
#     # 也可以使用open（）和close（）组合,但在不恰当时间关闭文件时程序将出错
#     contents = files.read()  # read读取文件，作为字符串存在contents中，
#     # 读的内容末尾多了空行，原因：read（)到达末尾时返回一个空字符串，而显示这个空字符串就是空行，可使用rstrip()去除
#     print(contents)
#     print("**************** Describe:88 *******************")
#     print(contents.rstrip())
#     # [Errno 2] No such file or directory: 'pi.txt' 文件放在file文件夹下，是否需要导入模块
#     # 文件放在同一个文件夹下，即chapter可以，原因：没有向python提供路径

"""
python转义字符
    \在行尾：续行符
    \\：反斜杠
    \'：单引号
    \":双引号
    \a:响铃
    \b:退格（backspace）
    \e:转义
    \000:空
    \n:换行
    \v:纵向制表符
    \t:横向制表符
    \r:回车
    \f:换页
    """
    # \oyy:八进制数，yy代表的字符，例如\o12代表换行
    # \xyy:十进制数，yy代表的字符，例如\x0a代表换行和ascii对应
    # \other:


# with open('K:\\project\\python_learn\\file\wx_pi_digits.txt') as file_object:
# #  表示路径要加双斜杠
#     content1 = file_object.read()
#     print(content1)

# with open('files\\pi.txt') as test1:  # 相对路径，在该py文件下一级
#     contest = test1.read()  # 文件里面有汉字会提示gbk代码解析问题，需要转码
#     print(contest)

# with open('python_learn\\file\\wx_pi_digits.txt') as test1:  #在该文件上一级无法解析，要用绝对路径
#     contest = test1.read()  #
#     print(contest)

print("**************** Describe:逐行读取 *******************")

print("**************** Describe:132 *******************")
# 创建一个包含文件各行内容的列表
#   方法：with代码块内部将各行存储在一个列表，在with代码块外部使用
# print(cache_file)

# with open('pi.txt') as file_object:
#     lines = file_object.readlines()  # 不用初始化，直接用
#     # line = file_object.readline()
# print(lines)
# print(line)
# python读取文本时，解读为字符串，如果你要使用数值，用int()或者float()转换
# python对处理的数据量没有限制

cache_file = []
pi_string = ''
with open('files\\pi.txt') as test_file:
    lines = test_file.readlines()

for line in lines:
    pi_string += line.rstrip()
# pi_string = ''
with open('files\\pi.txt') as test_file:
    lines = test_file.readlines()

for line in lines:
    pi_string += line.rstrip()

# birthday = input("请输入你的生日，按照格式mmddyy：")
# if birthday in pi_string:
#     print("你的生日在圆周率一万位里面")
#     print(pi_string.index(birthday))
# else:
#     print("你的生日不在圆周率一万位里面")

print("替换学习")
message = " I really like dogs"
# replace 只是临时替换而已
print(message.replace('dogs', '小孩'))
print(message)

file_name = "files\\test_write.txt"
str_len = 0
num = 0
last_num = len(pi_string)%80
print("pi修改前字符串长度：" + str(len(pi_string)))
with open(file_name, 'w') as file_object:  # 注意python只能将字符串写入文本，如果你要写int用str()
    for line in range(int(len(pi_string)/80)):
        file_object.write(pi_string[str_len: (str_len +80)] + "\n")
        str_len +=80
        num += 1
    file_object.write(pi_string[str_len:last_num+str_len] + "\n")
    # print(num)
    file_object.closed


pi_string1 = ''
with open('files\\test_write.txt') as file1:  # 刚开始file1和file——object重名，提示文件已经关闭，以后不能重名
    lines1 = file1.readlines()

for line in lines1:
    pi_string1 += line.rstrip()
print("pi重新写的文件字符串长度：" + str(len(pi_string1)))
"""
* Learn End ! 
* Time    : 2017/11/7 0:31
* Page    : 95
* Comment : 泡个脚，睡觉
"""

"""
* Learn Start !
* Time : 2017/11/7 0007 19:35
* Page : 95
* Comment : 
"""
"""
文件读写操作
    1.'w' 以写入模式打开这个文件 写入模式是重写整个文件
    2.'r' 以读取模式打开文件 
    3.'a' 以附加模式打开   附加模式可以在原来基础之上附加值
    4.'r+' 以读取和写入模式打开
    如果省略则默认以只读模式打开文件
"""
print("**************** Describe:异常处理 *******************")
# python使用被称为异常的特殊对象来管理程序执行期间发生的错误，每当发生让python不知所措的错误时
# 它都会创建一个异常对象，如果你处理了异常，程序继续运行，反之则停止

try:
    print("qulusheng" + 2)
except:
    print("类型错误")
else:
    print("正确")

try:
    print("qulusheng" + str(2))
except:
    print("类型错误")
else:
    print("正确")

# TypeError: must be str, not int
# TypeError是一个异常对象，python无法按照你要求运行时就会创建异常对象



"""
计算一本书单词量的函数
"""
def count_words(file_name):
    try:
        with open(file_name_alice) as f_obj:
            f_obj_contents = f_obj.read()
    except:
        msg = " Sorry, the file" + file_name_alice + "does not exist !"
        print(msg)
    else:
        words = f_obj_contents.split()
        num_words = len(words)
        print("The file" + file_name_alice + "has about " + str(
            num_words) + " words .")


file_name_alice = "files\\Alice in Wonderland.txt"
count_words(file_name_alice)  # 调用函数，计算单词数

# 异常时如果不处理可以用pass
"""
* Learn End !
* Time : 2017/11/7 0007 20:21
* Page : 100
* Comment : go home!
"""

