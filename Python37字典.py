#coding:utf-8
score = {
    '萧峰':95,
    '段誉':97,
    '虚竹':89
    }
print score['段誉']

for name in score:
    print score[name]

#改值
score['虚竹']=91

#加值
score['慕容复']=88

#删除值
del score['萧峰']
print score
#建一个空的字典
d={}