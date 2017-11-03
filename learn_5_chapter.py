"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习
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

print("**************** Describe:26 *******************")
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

print("**************** Describe:39 *******************")
#  检查特定值是否包含在列表中用in
t41 = ['t1', 't2', 't3', 't4', 't5']
print('t1' in t41)
print('t6' not in t41)
print('t6' in t41)

isTrue = True
print('isTrue : ' + str(isTrue))

print("**************** Describe:50 *******************")
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

print("**************** Describe:65 *******************")
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
print("**************** Describe:110 *******************")

for name in favorite_languages.values():
	print(name.title())
print("**************** Describe:107 *******************")
for name in favorite_languages:
	print(name.title())
# 默认遍历key

"""
* Learn End !
* Time : 2017/11/4 1:10
* Page : 56
* Addr : 史各庄
"""