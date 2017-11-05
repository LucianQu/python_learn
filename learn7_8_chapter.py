"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习 7-8章节
# author  : qulus
# time    : 2017/11/4 0004 19:22
"""****************-*******************"""
import module_author_info as ai
from module_author_info import my_name as nm, my_age as ag
from module_author_info import *
# 调用其他模块的方法
#   导入整个模块，import module, 再通过module.method调用
#       python打开这个module，并将module的所有函数复制到这个程序中，我们看不到，python幕后复制

#   导入特定函数（显式导入直接调用），from module import method，可用句点分割导入任意数量的函数

#   导入全部函数, from module import *,这个和导入模块差不多，但调用时不用加模块名
#       注意导入大型非自己写的代码时，可能模块的函数名与自己名字一样，造成意向不到的事情，覆盖函数，
#       而不是分别导入所有

# 如果导入的函数名和本文件的重名或者函数名太长，可指定别名，需要在导入时指定
#   注意，如果导入时指定了函数的别名，则原来的名字就无法使用，调用要用别名

print("**************** Describe:用户输入和while循环 *******************")
# 通过获取用户输入并学会控制程序的运行时间，可编写出交互式程序
print("**************** Describe:input()*******************")
# message = input("Tell me something, and I will repeat it back to you:")
# print(message)
# print(input("请输入："))

# input()获取用户输入信息
"""
* Learn End ! 
* Time    : 2017/11/4 0004 19:30
* Page    : 61
* Comment : 早上10点半到现在，该回家了，媳妇不在家
"""
"""
* Learn Start ! 
* Time    : 2017/11/4 20:49
* Page    : 61
* Comment : 继续奋战
"""
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is you first name ?"
# name = input(prompt)
# print("\nHello, " + name + "!")

"""

print("**************** Describe:int() *******************")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is you age ?"
name = input(prompt)
age = int(name)
if age > 12:
    print("true")
print("age =  " + str(age))
print(age % 3)  # 求模 %

"""
"""* Python2.7输入用raw_input() *"""
print("**************** Describe:while循环 *******************")
number = 1
while number <= 5:
    print(number)
    number += 1
    number = number + 1

"""
while true:
    break
while isTrue:
    isTrue = Fales
break 结束整个循环
continue 结束本次循环，回到循环开头继续执行，不结束整个循环
for循环是遍历列表的方式，但不应该修改列表，否则将导致python难以跟踪其中的元素
要在遍历列表的同时修改元素，可以用while循环
"""
t57 = ['t1', 't2', 't3', 't4', 't5']
n = 1
while t57:
    print(t57)
    n += 1
    if n == 10:
        break
# print(t57.pop()),当t57元素全部弹出时，while结束循环

print(t57)

"""
for循环和while循环格式一样
    for value in values:
    while value in values:
"""
print("**************** Describe:函数 *******************")

# 定义函数用 def

def hello_world1(value, value1):  # 定义的函数上面要有两个空行，不然提示希望有两个空行
    print(value + value1)

def hello_world(value):  # 定义的函数上面要有两个空行，不然提示希望有两个空行
    print(value)
    
"""* 注意：当定义两个相同的函数时，函数调用执行按照后面的那个调用，android可以名字相同 *"""

hello_world1(2+3, 0)
hello_world(2)
hello_world("qulusheng")
hello_world1([1, 2], ['t1', 't2', 't3', 't4', 't5'])  # int类型可以和字符类型相加在列表
hello_world(['t1', 't2', 't3', 't4', 't5'])
hello_world(['t1', 't2', 't3', 't4', 't5'])
hello_world({
    'te1': 'te1',
    'te2': 'te2',
    'te3': 'te3',
})
print("**************** Describe:91 *******************")
tee = ['1', '2'] + ['3', '4']  # 列表可以相加
print(tee)

"""* 形参和实参 函数调用时传入的是实参，函数定义的是形参*"""
print("1" + str(23))  # 打印函数字符串和int类型不能混用，必须用str转一样的
print(23 + int(1))
# 基于实参的顺序关联形参和实参，称为位置实参
def test1(name, age):
    print(name + age)

test1("qulusheng", "23")
test1("23", "qulusheng")
test1(name="qulusheng", age="23")
test1(age="23", name="qulusheng")  # 当加入关键字实参时，调转顺序不影响结果，python能识别

print("**************** Describe:112 *******************")
# 形参默认值
def test3(name, sex="girl", age="28"):  # 形参可以指定默认值，但必须跟着非默认，即默认的在后面
    # 等号两边不用空格，当用关键字参数时
    print(name + "-" + sex + "-" + age)

test3("qulusheng", "boy", "26")
test3("qulusheng", "boy")
test3("qulusheng")

"""
* Learn End ! 
* Time    : 2017/11/4 23:12
* Page    : 70
* Comment : 今天结束，玩会游戏，睡觉，明天继续奋战
"""
"""
* Learn Start ! 
* Time    : 2017/11/5 15:36
* Page    : 70
* Comment : 睡到中午，下午买个菜，剪个头发到现在
"""
# 位置实参，关键字实参和默认值可混用
# 函数返回值通过return来实现
def test(value):
    return value
value = test(12)
print(value)

# 让实参变成可选的
# 目的：使用函数的人只需要在必要时才提供额外的信息，可使用默认值""让实参变成可选
def getName(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + last_name + middle_name
    else:
        full_name = first_name + last_name
    return full_name
print(getName('qu', 'lu', 'sheng').title())  # 注意，当调用的函数无返回值时，打印None
print(getName('qu', ' lu').title())  # 注意，如果两个字符串中间有空格，则每个单词首字母大写
# 切片的结果是原来列表的副本
# 场景：处理列表，并保留原始数据
# 除非有充分理由，尽量还是用原来列表，因为创建副本需要花时间和内存，影响效率，特别是处理大型列表

"""* 传递任意数量的实参 *"""
# python允许函数从调用语句中收集任意数量的实参,并以"(1,2)"的形式存储，可通过[x]调用或者for循环遍历
def make_pizza(*topping):  # 注意topping前面的*号，让python创建一个空元组
    print(topping[0])
    print(topping)
    if len(topping) >= 2:
        print(topping[1])
make_pizza('1')
make_pizza('1', '2')
make_pizza('1', '2', '3')
# 综合使用位置实参和任意数量实参
# 函数接收不同类型实参，必须让任意数量实参（*）放在最后，python先匹配位置实参和关键字实参，
# 再将余下的实参都收集到最后一个形参中

print("**************** Describe:任意数量的关键字实参 **user_info *******************")
# 接收任意数量实参，不知道传递什么信息，将函数编写成能接收任意数量的键值对，调用语句提供了多少就接受多少
# 创建用户简介，不知道接收具体信息
te178 = {
    'te1': 'te1',
    'te2': 'te2',
    'te3': 'te3',
}
def build_profile(first, last, **user_info):  # 两个*让python创建一个名为user_info的空字典
    profile = {}  # 创建字典
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value1 in user_info.items():
        profile[key] = value1
    return profile
# user_profile = build_profile('qu', 'lusheng', te178)  # 错误，te178必须以关键字实参的形式传递进去
user_profile = build_profile('qu', 'lusheng', age='28')  # 错误，te178必须以关键字实参的形式传递进去
print(user_profile)

print("**************** Describe:模块 *******************")
# 将函数存储在一个独立的文件中，再将模块导入到主程序中，import语句允许在当前运行的程序文件中使用模块中的代码
# 通过模块，可以隐藏细节，重点放在高层逻辑（个人理解应用层），还能在不同程序中重用函数，还可和其他程序员共享
# 还可导入其他程序员的函数库
print("**************** Describe:导入模块的方法 *******************")

# author_info.my_name()  # 模块方法调用(import)，导入整个模块，调用 模块.方法
# my_name()  # 模块方法调用(from import)，方法
# my_age()

# 使用as给函数指定别名
ag()  # 别名调用
nm()   # 别名调用
ai.my_age()
ai.my_name()
print("**************** Describe:函数编写指南 *******************")
"""
1.函数小写和下划线，描述性名称
2.功能性注释，放在定义的函数后面
3.给形参指定默认值时，等号两边不要有空格，函数调用时的关键字实参也应遵循
4.形参过多时
    def function_name(
            parameter_0,parameter_1,
            parameter_2,parameter_3):  # 左边两个tab，8个空格
5.除了文件注释描述外，import应该放在文件开头
"""

