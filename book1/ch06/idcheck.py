#!/usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits

print 'Testees must by at least 2 character long'

myInput = raw_input('sample is: ')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print 'first character must be alphabetic'
    else:
	for x in myInput[1:]:
	    if x not in alphas:
		print 'invalid remaining symbols'
		break
	print 'symbols are alphabetical'
     
