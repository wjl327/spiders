__author__ = 'Administrator'

myfile = open('myfile.txt', 'w')
for i in range(1,11):
    myfile.write("hello - " + str(i) + "\n")
myfile.close()