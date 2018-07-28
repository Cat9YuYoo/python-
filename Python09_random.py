#coding:utf-8
from random import randint#from 模块名 import 方法名

randint(5,10)#产生一个5到10之间（包括5和10）的随机数

num=randint(1,100)
print 'Guess what I think?'
bingo=False
while bingo==False:
    answer=input()
    if answer<num:
        print 'too small'

    if answer>num:
        print 'too big'

    if answer==num:
        print 'BINGO'


