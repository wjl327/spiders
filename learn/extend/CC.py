__author__ = 'Jarvis.Wu'
__metaclass__ = type

class A:
    def __init__(self):
        print "A"

class B:
    def __init__(self):
        print "B"

class C(A,B):
    def __init__(self):
        super(C, self).__init__()
        print "C"

c = C()