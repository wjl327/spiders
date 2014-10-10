__author__ = 'Administrator'

myfile1 = open("myfile.txt", "r")
myfile2 = open("myfile_copy.txt", "w")
while True:
    line = myfile1.readline()
    myfile2.write(line)
    if not line:
        break

myfile1.close()
myfile2.close()