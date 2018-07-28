#coding:utf-8

#输出5个*，如果要5个*在同一行，就在print语句后面加上逗号

for i in range(0,5):
    print '*'

for i in range(0,5):
    print '*',

for i in range(0,5):
    for j in range(0,5):
        print i,j


#print 后面没有任何东西，是起到换行的作用
for i in range(0,5):
    for j in range(0,5):
        print'*',
    print


#输出三角形
for i in range(0,5):
    for j in range(0,i+1):
        print '*',
    print