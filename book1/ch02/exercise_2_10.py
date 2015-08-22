#!/usr/bin/env python

get_out = False
i = 0
while get_out == False:
	num = raw_input('Enter number between 1 and 100: ')
	i = int(num)
	if i > 0 and i < 100:
		get_out = True
	else:
		print 'Error: number is outside the range'
print 'number is: {0}'.format(i)


