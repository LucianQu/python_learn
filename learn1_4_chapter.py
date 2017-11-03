"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习
# author  : QLS
# time    : 2017/11/2 23:04
"""****************-*******************"""

# import this社区之禅
"""****************-字符串*******************"""

"""*-字符串首字母大写*"""
message = "hello python"
print(message.title())

"""*-字符串全部小写*"""
message = "hello python"
print(message.lower())

"""*-字符串全部大写*"""
message = "hello python"
print(message.upper())

"""*-字符串拼接*"""
first_name = "qu"
last_name = "lusheng"
full_name = first_name + " " + last_name
print(full_name)

"""*-字符串添加制表符Tab*"""
print("\thelloworld")

"""*-字符串添加换行符*"""
print("hello\nworld")

"""*-删除字符串末位空白*"""
message = "helloWorld "
print(message.rstrip())
print(message)
message = message.rstrip()
print(message)

"""*-删除字符串开始空白*"""
message = " helloWorld"
print(message.lstrip())

"""*-删除字符串两端空白*"""
message = " helloWorld "
print(message.strip())

"""*-Python2中print语句有些包含括号，有些不包含，Python3则包含，Python3中的print是一个函数*"""

"""****************-整数*******************"""
da = 2 ** 3
print(da)

da = 0.1 + 0.5
print(da)

age = 23
message = "my age is :" + str(age)
print(message)

da = 3 / 2
print(da)

da = 7 / 3
print(da)

"""****************-列表or数组*******************"""
buff = ['ce1', 'ce2', 'ce3']
print(buff)
print(buff[1])

buff = {'1', '2', "3"}
print(buff)
# print(buff[0]) 错误

# buff = {{'1', '2', "3"}, {'1', '2', "3"}, {'1', '2', "3"}}
# print(buff)错误，终止程序运行

# buff = {['ce1', 'ce2', 'ce3'], ['ce1', 'ce2', 'ce3'], ['ce1', 'ce2', 'ce3']}
# print(buff)错误，程序会终止这里

buff = [{'1', '2', "3"}, {'4', '5', "6"}, {'7', '8', "9"}]
print(buff[1])
print(buff[1])
print(buff[1])

buff = [['ce1', 'ce2', 'ce3'], ['ce4', 'ce5', 'ce6'], ['ce7', 'ce8', 'ce9']]
print(buff[1][0])

"""*-返回列表最后一个元素，用-1*"""
print(buff[0][-1])
buff[0] = ['', '', '1']
print(buff[0])

"""*-在列表追加数据*"""
buff.append(['1', '2', '3'])
print(buff)

"""*-在列表指定位置移除数据*"""
buff.remove(buff[0])
print(buff)
# buff.clear()
# print(buff)

buff = ['ce1', 'ce2', 'ce3']
"""*-在列表指定位置插入数据*"""
buff.insert(1, '7')
print(buff)

"""*-删除列表指定位置数据*"""
del buff[0]

print(buff)

pop_last = buff.pop()  # 弹出最后一个数据，指出最后一个进栈的数据
print(pop_last)
print(buff)

"""*-弹出任意位置数据*"""
buff = ['ce1', 'ce2', 'ce3', 'ce3', 'ce3']
pop_everyWhere = buff.pop(1)
print(pop_everyWhere)
print(buff)

"""*-根据值删除内容*"""
buff.insert(1, "ce2")
buff.remove("ce3")  # 移除第一次出现的位置，从索引0开始找
print(buff)
"""*-*"""
"""****************-组织列表*******************"""
cars = ['1', '2', '5', '4']
print(cars)
"""*-对列表进行永久排序*"""
"""
    排序时，如果有大写字母，先排大写字母，再排小写字母
"""
"""*-正向永久排序*"""
cars.sort()
print("****************Line:正向排序*******************")
print(cars)
"""*-逆向永久排序*"""
cars.sort(reverse=True)
print(cars)
"""*-临时排序sorted()*"""
print(sorted(cars))
print(cars)
"""*-倒着打印列表,永久性*"""
cars.reverse()
print(cars)
"""*-确定列表长度*"""
length = len(cars)
print(length)
"""
Python计算列表长度是从1开始，索引是从0开始，没毛病
任何时候都可以用-1访问最后一个元素，只有列表为空时才会错误用-1
"""

"""****************-遍历列表for循环*******************"""
bfs = ['1', '2', '3', '4']
for bf in bfs:
    print(bf)  # python根据缩进判断代码和前一个代码行的关系，因此缩进不能任意进行
    print(bf)
print(bf)  # 使用for循环遍历一个角色列表，最后一个不缩进的代码块绘制一个play now按钮

print("****************Line:166*******************")
"""*-创建数值列表*"""
for value in range(1, 5):
    print(value)

"""* 使用range创建数字列表 *"""
numbers = list(range(1, 6))
print(numbers)
"""* [1, 2, 3, 4, 5] *"""

even_numbers = list(range(1, 10, 2))
print(even_numbers)

even_numbers = list(range(2, 10, 2))
print(even_numbers)

even_numbers = list(range(3, 10, 5))
print(even_numbers)

squares = []  # 创建一个空的列表
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)
print("****************Line:189*******************")

"""* 对数值列表进行简单的统计 *"""
print("最小值：" + str(min(squares)))
print("最大值：" + str(max(squares)))
print("数值的和：" + str(sum(squares)))
print("****************Line:194*******************")

"""* 列表解析 *"""
squares = [value + 10 and value ** 2 for value in range(1, 10)]
print(squares)
#  语法介绍：指定一个描述性的列表名，如squares，定义表达式value ** 3，for循环给表达式提供值，只能有一个表达式，隐藏了append
#  for循环结尾没有冒号：
tests = [value for value in range(3, 30, 3)]
for value in tests:
    print(value)

print("****************Line:测试立方根*******************")
for value in range(3, 30, 3):
    print(value)
for value in range(1, 10):
    print(value * value ** 2)
"""**************** 使用列表的一部分俗称切片 *******************"""
players = ['要命', '要洗', '要查', 'yaohe']
print(players[0: 2])  # :前出现空格，会提示，同时线注释至少两个空格
print(players[:4])  # 如果么有指引第一个索引，则python自动从头开始
print(players[0:])  # if no index the last ,default to end
print(players[-1:])
print(players[-2:])  # -x 代表从后面往前面数几位
print(players[:])
"""
#  场景：编写游戏时，你可以在玩家退出游戏时将其最终得分加入到一个列表，然后为获取该玩家的三个最高分，
#  sort(reverse=True)可以降序或者升序排列列表，在获取后三个切片，
#  编写web程序时，可分页显示信息，并在每页显示数量合适的信息
"""
"""* 复制lieb *"""
player1 = players[:]
print("**************** Describe:复制列表 *******************")
print(player1)
player1.append('ce')
print(player1)
print(players)
# 注意：如果player1不使用切片，则player1和players指向同一个变量，使用切片，则是把copy了一份给player1，如果新变量添加元素，
# 就代码老变量也添加元素
test1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lens = len(test1)
lens2 = lens // 2
print(lens2)
print(test1[(lens2 - 1): (lens2 + 2)])

"""**************** 元组 *******************"""
# 列表非常适合用于存储在程序期间可能变化的数据集，这对于处理网站的用户列表或者游戏中的角色至关重要
# 然而有时需要创建一系列不可修改的元素，元组可以满足这种需求，python将不可修改的值称为不可变，而不可变的列表称为元组
"""
* Learn Start ! 
* Time : 2017/11/3 21:13
* Page : 41
* Addr : Automic
"""

"""
* Learn Start ! 
* Time : 2017/11/3 23:07
* Page : 41
* Addr : 史各庄
"""
# 元组使用圆括号括起来，定义元组后可以使用索引访问
print("**************** Describe:249 *******************")
dimension = (200, 50)
print(dimension[0])
# dimension[0] = 100  TypeError: 'tuple' object does not support item assignment
# 遍历方法和列表一样



