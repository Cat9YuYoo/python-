#coding:utf-8
import random

num=random.randint(1,100)
#随机整数

random.random()
#随机浮点数

random.uniform(1.6,3)
#随机浮点数


random.choice([1,2,3,4,5,7,87])
random.choice('hello')
random.choice(['hello','world'])    
random.choice((1,2,3))
#序列中随机选取一个元素

random.randrange(1,9,2)
#random.randrange(start,stop,step)
#生成一个从start到stop（不包括stop），间隔为step的一个随机数
#start、stop、step都为整数，且start<stop
random.randrange(4)
#start和step默认从0开始，间隔为1

#random.sample(p,k)
#从p序列中随机k个元素，生成新序列，不改变原序列

#random.shuffle(x)
#把序列x中 的元素顺序打乱

random.seed(7)