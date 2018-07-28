#coding:utf-8
l=[365,'everday',0.618,True]

#访问list中的元素
print l[1]

#修改list中的元素
l[0]=123
print l

#向list添加元素
l.append(1024)
print l

#删除list中的元素

del l[0]
print l


#罚球游戏

from random import choice
print 'Choose one side tp shoot:'
print 'left,center,right'
you=raw_input()
print 'You kicked '+you
direction=['left','center','right']
com=choice(direction)
print 'Computer saved '+com
if you!=com:
    print 'Goal!'
else:
    print 'Oops...'

#list 的负索引
l=[365,'everday',0.618,True]
print l[-1] #最后一个元素
print l[-3]#倒数第三个元素

#切片操作符
#用：分割，冒号前的数表示切片的开始位置，
#冒泡后的数字表示切片到哪里结束
#如果不指定第一个数切片从列表第一个元素开始
#如果不指定第二个数，就一直到最后一个元素结束
#都不指定，则返回整个列表的一个拷贝#
print l[1:3]
l[:3]
l[1:]
l[:]
l[1:-1]

#game

from random  import choice
score_you=0
score_com=0
direction=['left','center','right']
for i in range(5):
    print '===Round %d-You Kick!===='%(i+1)
    print 'Choose one side to sshoot:'
    print 'left,center,right'
    you =raw_input()
    print 'You kicked '+you
    com=choice(direction)
    print 'Computer saved '+com
    if you !=com:
        print 'Goal!'
        score_you+=1
    else:
        print 'Oops...'
    print 'Score: %d(you)-%d(com)\n' % ( score_you, score_com)

    print'===Round %d - You Save!===='%(i+1)
    print 'Choose one side to save:'
    print"left,center,right"
    you =raw_input()
    print'You saved '+you
    print'Computer kicked '+com
    if you==com:
        print 'Saved!'
    else:
        print 'Oops...'
        score_com+=1
    print 'Score: %d(you) - %d(com)\n' %(score_you,score_com)