#!/usr/bin/env python

''' readNwriteTextFiles.py -- create and read text file
    options:
    'i' followed with line number - insert a line 
    'e' followed with line number - edit a line
    'p' - print whole file
    any character than abowe - exit
 '''

import os
ls = os.linesep

def insertLineNum(option):
    if option == 'i' or option == 'e':
        linenum = int(raw_input('Enter the line number: '))
        if not isinstance(linenum, int):
            print "error: must be number "
            exit()
        else:
            return linenum
    elif option != 'p':
        return 0
    return 1

def editFile():
    filename = raw_input('Enter file name: ') 
    handler = open(filename, 'a+')
    text = []
    for line in handler:
        text.append(line)

    # loop until user terminates
#    import pdb; pdb.set_trace()
    while True:
        option = raw_input("Enter the option: 'i' insert line, 'e' edit line, 'p' print file, any other char will exit")
        linenum = insertLineNum(option)
        if option == 'p':
            for l in text:
                print l,
        elif linenum == 0:
            break
        else:
            entry = raw_input('> ')
            entry = '{0}{1}'.format(entry, ls)
            if option == 'i':
                text.insert(linenum-1, entry)
            elif option == 'e':
                text[linenum-1] = entry 

    # write all lines to file with proper line-ending
    handler = open(filename, 'w')  
    handler.writelines(['{0}'.format(x) for x in text])
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

option = raw_input("Enter the read/edit option: ")
if option == 'read':
    readFile()
elif option == 'edit':
    editFile()
else:
    print "Correct options are 'read' or 'edit'"
