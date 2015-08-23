#!/usr/bin/env python

' makeTextFile.py -- create text file'

import os
ls = os.linesep

filename = raw_input('Enter file name: ') 
try:
    handler = open(filename, 'w')
except IOError, e:
    print "*** file opening error: ", e

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

