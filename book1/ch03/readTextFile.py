#!/usr/bin/env python

' readTextFile.py -- read text file'

import os

filename = raw_input('Enter file name: ')

# open the file
try:
    handler = open(filename, 'r')
except IOError, e:
    print "file open error:", e
else:
    for line in handler:
        print line,
    handler.close()
