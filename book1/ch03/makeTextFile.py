#!/usr/bin/env python

' makeTextFile.py -- create text file'

import os
ls = os.linesep

while True:
    filename = raw_input('Enter file name: ') 
    if os.path.exists(filename):
        print 'error: filename {0} already exists'.format(filename)
    else:
        break

text = []
print "\nEnter lines ('.' to quit).\n"

# loop until user terminates
while True:
    entry = raw_input('> ')
    if entry == '.':
	break
    else:
        text.append(entry)

# write all lines to file with proper line-ending
handle = open(filename, 'w')  
handle.writelines(['{0}{1}'.format(x, ls) for x in text])
handle.close()
print 'DONE!'

