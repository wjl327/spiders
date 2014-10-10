__author__ = 'Administrator'

import fileinput

myfile = open("myfile.txt", 'r')
print myfile.readlines()
myfile.close()

print

for line in fileinput.input("myfile.txt"):
    print line