#__author:iruyi
#date:2018/9/18
import math

# old method first kind of format string --use %
print("The value is %5.4f" % math.pi)

#second kind of format string -- use f or F
year = 2016
event = '足球'
value = f'Results of the {year} {event}'
print(value)

#third kind of format string -- str.format()
test = 'Results of the {0} {1}'.format(year,event)
print(test)


#distinction between str() and repr()
#str() human-readable
#repr() better for interpreter
#same for many values, such as numbers ，lists,dictionaries
#diference in Strings

s = 'Hello,World'
print('str() is ',str(s))
print('repr() is ',repr(s))
x = 1/7
print('str() is ',str(x))
print('repr() is ',repr(x))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

#fourth str.rjust() a field of a given width by padding it with spaces on the left
print('str.rjust() ---------------------')
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))

#str.zfill() which pads a numeric string on the left with zeros, it understands about plus and minus signs
print('str.zfill()-------------')
print('12'.zfill(5))
print('-3.14'.zfill(8))
