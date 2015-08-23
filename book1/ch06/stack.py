#!/usr/bin/env python
'''
An example of using list as a text stack
'''

stack=[]

def pushit():
    stack.append(raw_input('Enter new string: ').strip())

def popit():
    if len(stack) == 0:
        print "There is nothing in stack"
    else:
        stack.pop()
        print 'Removed [', 'stack.pop()', ']'

def viewstack():
    print stack

CMDs = {'u': pushit, 'o': popit, 'v': viewstack}

def showmenu():
    pr = """
p(u)sh
p(o)p
(v)iew
(q)uit

Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print 'You picked option: {0}'.format(choice)
            if choice not in 'uovq':
                print 'Invalid option, try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()	
    

