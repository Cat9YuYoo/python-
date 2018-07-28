#coding:utf-8
#x>=0,y>=0,输出1;
#x<0,y>=0,输出2;
#x<0,y<0,输出3;
#x>=0,y<0,输出4.
##
x=-1
y=-1
if y>0:
    if x>=0:
        print 1
    else:
        print 2
else:
    if x<0:
        print 3
    else:
        print 4


