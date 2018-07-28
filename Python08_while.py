#coding:utf-8
#这是注释

a=1#先a设为1
while a!=0:#a不等于0就一直做
    print "please input"
    a=input()
print "over"

num=10
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
