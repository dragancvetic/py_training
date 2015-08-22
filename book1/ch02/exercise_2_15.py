#!/usr/bin/env python

ls = []
for i in range(3):
	ls.append(int(raw_input('Enter number: ')))
if ls[0] > ls[1] and ls[0] > ls[2]:
	if ls[1] > ls[2]:
		print 'order is 1, 2, 3'
	else:
		print 'oder is 1, 3, 2'
elif ls[1] > ls[0] and ls[1] > ls[2]:
	if ls[0] > ls[2]:
		print 'order is 2, 1, 3'
	else:
		print 'oder is 2, 3, 1'
elif ls[0] > ls[1]:
	print 'order is 3, 1, 2'
else:
	print 'oder is 3, 2, 1'


