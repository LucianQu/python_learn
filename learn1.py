"""****************-*******************"""
# describe: 测试工程
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


