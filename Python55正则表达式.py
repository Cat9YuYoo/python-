#coding:utf-8
import re
text='Hi, I am Shirley Hilton. I am his wife.'
m=re.findall(r"hi",text)
if m:
    print m
else:
    print 'not match'

#\b表示单词的开头或结尾
#[]表示满足括号中任一字符
#比如[hi]就不是匹配"hi"了，而是匹配"h"或者"i"
#[Hh]i 可以匹配Hi又可以匹配hi
#
#
##

print r"\bhi"
print "\bhi"
#r表示不要去转义字符串中的任何字符
##

re.findall(r"hi",text)
#re是python里的正则表达式模块findall是其中一个方法
#用来按照提供的正则表达式，去匹配文本中的所有符合条件的字符串。
#返回结果是一个包含所有匹配的list
##

#“ . ”" * " 
#" . "表示除换行符以为的任意字符

m=re.findall(r"i.",text)
print m
m=re.findall(r".",text)
#print m

#?表示任意一个字符
# .表示任意字符，*表示前面的字符可以重复多少次，包括0次
#
#\S表示的是不是空白符的任意字符，大写S
##


#匹配数字
#
#[0123456789]
#简化写法[0-9],类似的有[a-zA-z]
#\d
#表示任意长度的数字[0-9]*或\d*
#*会把空字符也匹配出来
#+表示的则是1个或更长
#[0-9]+或\d+
#
#要限定长度用{\d}
#\d{11}
#想要限定第一位为1
#1\d{10}
##