import sys


def sys_input(names) :
    if len(sys.argv) > 1:
        print "Hello",
        for name in names:
            print name + "!" ,
    else:
        print "Hello World!"
sys_input(sys.argv[1:])
