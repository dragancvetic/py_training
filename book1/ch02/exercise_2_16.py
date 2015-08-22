#!/usr/bin/env python

fname = raw_input('Enter file name: ') 
handle = open(fname, 'w')  
str = raw_input('Enter string into file: ')
handle.write(str)
handle.close()

handle = open(fname, 'r')  
for eachLine in handle:
	print eachLine 
