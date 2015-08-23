#!/usr/bin/env python

' readNwriteTextFiles.py -- create and read text file'

import os
ls = os.linesep

def writeFile():
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
    handler = open(filename, 'w')  
    handler.writelines(['{0}{1}'.format(x, ls) for x in text])
    handler.close()
    print 'write to file DONE!'

def readFile():
    filename = raw_input("Enter file name: ")
    try:
        handler = open(filename, 'r')
    except IOError, e:
        print '*** error: file {0} does not exist'.format(filename)
    else:
        for line in handler:
            print line,
        handler.close()

option = raw_input("Enter the read/write option: ")
if option == 'read':
    readFile()
elif option == 'write':
    writeFile()
else:
    print "Correct options are 'read' or 'write'"
