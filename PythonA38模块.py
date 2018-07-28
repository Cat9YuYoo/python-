#coding:utf-8
#使用模块
import random
print random.randint(1,10)
print random.choice([1,3,5])

#想知道random有哪些函数和变量可以用dir()方法：
#print dir(random)

#用到random中的一个函数或变量
from math import pi
print pi

#可以给方法换个名字
from math import pi as math_pi

print math_pi
