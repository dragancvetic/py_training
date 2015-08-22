#!/usr/bin/env python

str = raw_input('Enter string: ')
print "while loop"
i = 0
while i < len(str):
	print str[i]
	i += 1
print "for loop"
for i in range(len(str)):
	print str[i]


