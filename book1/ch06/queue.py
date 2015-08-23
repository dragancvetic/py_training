#!/usr/bin/env python
'''
An example of using list as a text queu
'''

queue=[]

def enQ():
    queue.append(raw_input('Enter new string: ').strip())

def deQ():
    if len(queue) == 0:
        print "There is nothing in queue"
    else:
        queue.pop(0)
        print 'Removed [', 'queue.pop()', ']'

def viewstack():
    print queue

CMDs = {'e': enQ, 'd': deQ, 'v': viewstack}

def showmenu():
    pr = """
(e)nqueue
(d)equeue
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
            if choice not in 'edvq':
                print 'Invalid option, try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()	
    

