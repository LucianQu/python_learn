"""****************-*******************"""
# describe: 《Python编程：从入门到实践》学习 10-章节
# author  : QLS
# time    : 2017/11/7 21:15
"""****************-*******************"""
"""
* Learn Start ! 
* Time    : 2017/11/7 21:16
* Page    : 100
* Comment : 
"""
import json
import unittest

print("**************** Describe:存储数据JSON格式 *******************")
# json模块能够让你将简单的python数据结构存储到文件中，并在程序再次运行时加载该文件中的数据，
# 还可以用json在python程序之间分享数据
# JSON JavaScript Object Notaiton
# json.dump(data, save_object)存储
# json.load()加载

numbers = ['1', '2', '3']
file_name_json = "files\\numbers.json"
with open(file_name_json, 'w') as json_obj:
    json.dump(numbers, json_obj)  #  (data, object)
    # 输出结果：["1", "2", "3"] 注意输出由单引号变为双引号

with open(file_name_json) as json_obj1:
    numbers1 = json.load(json_obj1)
print("读取json结果: " + str(numbers1))  # 返回json结果以列表形式返回

"""
定义：
    1.单元测试：用于核实函数的某个方面没有问题
    2.测试用例：是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求
    3.
"""
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        name = "Qu Lu Sheng"
        self.assertEqual(name, "Qu Lu Sheng")

    def test_first_last_name1(self):
        name1 = "Qu Lu Sheng"
        self.assertEqual(name1, "Qu Lu Sheng")

    def ftest_first_last_name2(self):
        name2 = "Qu Lu Sheng"
        self.assertEqual(name2, "Qu Lu Sheng")
    # 注意测试方法必须以test_开头，程序运行测试类时才会执行

unittest.main()  # 运行测试  Ran 1 test in 0.000s  OK  1代表数量，1个测试

"""
断言方法介绍：
    1.assertEqual(a, b) 核实 a == b
    2.assertNotEqual(a, b) 核实 a != b
    3.assertTrue(x) 核实 x 为true
    4.assertFalse(x) 核实 x为false
    5.assertIn(item, list) 核实item在list中
    6.assertNotIn(item, list) 核实item不在list中
"""
"""
* Learn End ! 
* Time    : 2017/11/7 22:55
* Page    : 108
* Comment : 累了，刷牙睡觉
"""