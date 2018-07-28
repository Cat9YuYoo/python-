#coding:utf-8

#无论你有多少个值需要带入字符串中进行格式化，只需要在
#字符串中的合适位置用对应格式的%表示，然后后面的括号中按顺序提供
#代入得值就可以
#占位的%和括号中的值在数量必须相等，类型也要匹配

#('Mike',87)这种用()表示的一组数据在python中被称为元组（tuple），
#是一种基本的数据结构
print "%s's score is %d"%('Mike',87)

#或者
name='Lily'
score=97
print "%s's score is %d" %(name,score)
