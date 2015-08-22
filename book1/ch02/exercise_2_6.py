#!/usr/bin/env python

i = raw_input('Enter first number: ')
j = raw_input('Enter second number: ')
if i < j:
	print "Number {0} is smaler than {1}".format(i,j)
elif i == j:
	print "Number {0} is same as {1}".format(i,j)
elif i > j:
	print "Number {0} is greater than {1}".format(i,j)


