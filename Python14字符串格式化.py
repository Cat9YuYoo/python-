#coding:utf-8

#字符串连接
str1='good'
str2='bye'
print str1+str2

#字符串和字符串变量连接
print 'vert'+str1
print str1+'and'+str2

#字符串和数字连接
#不能直接把字符串和数字直接相加 
#用str()把数字转换成字符串 
print 'My age is'+str(18)
#或
num =18
print 'My age is '+str(num)

#%对字符串进行格式化
#输出时，%d会被%后面的值替换
#%d只能替换整数，格式化小数用%f，想保留两位小数在f前加条件：%.2f
#%s可以替换一段字符串

num=18
print 'My age is %d' %num
print 'Price is %.3f' %4.99

name='Crossin'
print '%s is a good teacher.'%name
print 'Today is %s.' %'Friday'