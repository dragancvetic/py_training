#!/usr/bin/env python

' readTextFile.py -- read text file'

import os

filename = raw_input('Enter file name: ')

# open the file
while True:
    if os.path.exists(filename):
        handler = open(filename, 'r')
        break
    else:
        print "file {0} does not exist".format(filename)
for line in handler:
    print line,
handler.close()
