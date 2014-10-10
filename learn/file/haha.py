myfile = open("haha.txt", "r")

while True:
    line = myfile.readline()
    if not line:
        break
    print(line[8:])

myfile.close()
