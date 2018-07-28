a=1
if a==1:
    print 'right'
else:
    print 'wrong'


if a==1:
    print 'one'
elif a==2:
    print 'two'

if a==1:
    print 'one'
elif a==2:
    print 'two'
elif a==3:
    print'three'
else:
    print 'too many'



def isEqual(num1,num2):
    if num1<num2:
        print'too small'
        return False;
    elif num1>num2:
        print 'too big'
        return False;
    else:
        print 'bingo'
        return True;

from random import randint
num=randint(1,100)
print'Guess what i think?'
bingo=False
while bingo==False:
    answer=input()
    bingo=isEqual(answer,num)