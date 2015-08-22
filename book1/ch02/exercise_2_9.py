#!/usr/bin/env python

num = raw_input('Enter list size: ')
ls = []
for i in range(int(num)):
	ls.append(int(raw_input('Enter an element: ')))
print 'sum is: {0}'.format(sum(ls))
print 'average is: {0}'.format(float(sum(ls))/int(num))


