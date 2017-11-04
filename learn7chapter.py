"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习
# author  : qulus
# time    : 2017/11/4 0004 19:22
"""****************-*******************"""

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
* Comment : 今天结束，玩会王者，睡觉，明天继续奋战
"""

