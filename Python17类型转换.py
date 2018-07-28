#coding:utf-8

#字符串
#整数
#小数（浮点数）
#bool类型
#int(x)把x转换成整数
# float(x)转换成浮点数
#str(x)转换成字符串
# bool(x)转换成bool值
a=1
print a
a='hello'
print a
a=True
print a

print 'Hello'+str(1)
print 'hello%d' %int('123')

#以下结果均为真
int('123')==123
float('3.3')==3.3
str(111)=='111'
bool(0)==False