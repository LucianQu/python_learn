"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习 5-6章节
# author  : QLS
# time    : 2017/11/3 23:20
"""****************-*******************"""

"""**************** if语句学习 *******************"""
cars = ['bmw', 'benteng', 'audi', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':  # if和else结尾处都有：
        print('满足条件的车: ' + car.upper())
        print('满足条件的车: ' + car.upper())
    else:
        print('不满足条件的车: ' + car.title())
        print('不满足条件的车: ' + car.title())
car1 = 'and'
car2 = 'And'
car3 = 'and'
print(car1 == car2)
print(car1 == car3)
#  检查两个值是否相等，区分大小写
#  不相等用 ！=
print(car1 != car2)
print(car1 != car3)

print("**************** Describe:练习if else *******************")
age1 = 19
age2 = 20
#  多个条件时 && = and ， || = or
if (age1 <= age2) and (age1 < 19):
    print("this is true")
else:
    print("this is false")

if age1 <= age2 or age1 < 19:
    print("this is true")
else:
    print("this is false")

print("**************** Describe:练习 in， not in *******************")
#  检查特定值是否包含在列表中用in
t41 = ['t1', 't2', 't3', 't4', 't5']
print('t1' in t41)
print('t6' not in t41)
print('t6' in t41)

isTrue = True
print('isTrue : ' + str(isTrue))

print("**************** Describe:练习if语句 *******************")
age1 = 12
if age1 < 4:
    print('this is true age1 < 4')
elif age1 < 12:
    print('this is true age1 < 12')
else:
    print('this is true age1 >= 12')

tt = []
if tt:  # tt等于空时，if语句能自动判断
    print('[]')
else:
    print('0')

print("**************** Describe:练习for循环 *******************")
t66 = ['t1', 't2', 't3', 't4', 't5']
t67 = ['t1', 't2', 't3', 't4', 't5', 't4', 't3', 't8', 't9']
tIsExist = []
tIsNotExist = []

for t7 in t67:
    if t7 in t66:
        if t7 not in tIsExist:
            tIsExist.append(t7)
    else:
        tIsNotExist.append(t7)
print('在列表中的' + str(tIsExist) + '\n')
print('不在列表中的' + str(tIsNotExist))

print("**************** Describe:使用字典 *******************")

# 花括号括起来的就相当于字典了
alien_0 = {'color': 'green', 'points': '5'}
# {}存储的类似键值对形式的值，通过key能获取：后面的值
print(alien_0['color'])

# 添加键值对
alien_0['sex'] = '男'
alien_0['age'] = 27
alien_0['age'] = 28  # 修改字典的值
del alien_0['age']  # 删除字典的值
print(alien_0)

# alien_0.clear()
favorite_languages = {
    'jen': 'python',
    'ben': 'java',
    'qulusheng': 'android',
}
print('qulusheng love languages is ' + favorite_languages['qulusheng'].title())
# print('qulusheng love languages is ' + favorite_languages['lucian'].title())
# 注意，如果未找到，则不执行

for key, value in favorite_languages.items():  # 默认格式吗，字典key value items()
    print("\nkey: " + key + '\nvalue:' + value)
print(favorite_languages.items())
# dict_items([('jen', 'python'), ('ben', 'java'), ('qulusheng', 'android')])
# 注意：Python不关心键值对存储的顺序

for name, languages in favorite_languages.items():
    print("\nname: " + name + '\nlanguages:' + languages)
"""* 注意：提供的第一个任意parm为key，第二个parm为value，任意的 *"""

for name in favorite_languages.keys():
    print(name.title())
# 可根据keys或者values或者items来提前字典内容
print("**************** Describe:遍历value *******************")

for name in favorite_languages.values():
    print(name.title())
print("**************** Describe:默认遍历key *******************")
for name in favorite_languages:
    print(name.title())
# 默认遍历key

"""
* Learn End !
* Time    : 2017/11/4 1:10
* Page    : 56
* Comment : 凌晨了，明天还要加班，苦逼
"""
"""
* Learn Start !
* Time    : 2017/11/4 0004 16:19
* Page    : 56
* Comment : 搞交城APP累了，歇会
"""

"""**************** 按照顺序遍历字典中的所有键 *******************"""
te140 = {
    't1': 't1',
    't2': 't2',
    't3': 't3',
    't4': 't4',
    't5': 't5',
}
for name in sorted(te140.keys(), reverse=True):  # 逆向排序,不改变原有的
    print(name)
print(te140.keys())  # dict_keys(['t1', 't2', 't3', 't4', 't5'])

"""**************** 集合set剔除重复项，集合的元素独一无二 *******************"""
te152 = {
    't1': 't1',
    't2': 't2',
    't3': 't3',
    't4': 't3',
    't5': 't3',
}
temp = set(te152.values())
for value in set(temp):  # set or sorted 用于创建临时列表，供for循环使用
    print(value)
print(temp)
print(te152)
print(set(te152.values()))

print("**************** Describe:嵌套 *******************")
print("有时需要将一系列字典{}存储在列表[]中，或者将列表[]存储在字典{}中，称为嵌套")

te169 = {
    't1': 't1',
    't2': 't2',
    't3': 't3',
    't4': 't4',
    't5': 't5',
}
te176 = {
    't1': 't1',
    't2': 't2',
    't3': 't3',
    't4': 't4',
    't5': 't5',
}

dicts = [te169, te176]
for value in dicts:
    print(value.keys())
lists = []
for item in range(30):
    listValue = {'position': item, 'value': item}
    lists.append(listValue)
    """
    
    """
print(len(lists))
"""打印lists长度，“”“”“”不能放在语句后面"""

for itemValue in lists[:5]:  # lists切片0-4位置的值
    print(itemValue)

print("**************** Describe:在字典中存储列表 *******************")
# 场景：描绘顾客点的披萨包含外皮类型和配料列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("you ordered a " + pizza['crust'] + " = crust pizza " +
      "with the following topping:")
for topping in pizza['toppings']:
    print("\t" + topping)  # \t 代表tab的意思

print("**************** Describe:字典中存储字典 *******************")
# 场景：网站有多个用户，每个用户有独立用户名，可在字典中将用户名作为key，然后将用户信息存储在
#      在一个字典中，字典关联key。
users = {
    'lucian': {
        'name': 'qulusheng',
        'age': 28,
    },
    'tony': {
        'name': 'quzishun',
        'age': 1.5
    },
}

for userName, userInfo in users.items():
    print("\nUserName: " + userName)
    print("真名：" + userInfo['name'])
    print("年龄：" + str(userInfo['age']))  # 注意age不是字符串，需要加上str()，不然错误，不执行
"""* 注意：字典嵌套字典，结构尽量相同，python没要求，但相同处理更容易，key不同则for循环内部代码更复杂 *"""

