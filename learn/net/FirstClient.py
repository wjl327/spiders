__author__ = 'Jarvis.Wu'

import socket

#host = socket.gethostname()
host = "localhost"
port = 12345

for i in range(1, 11):
    s = socket.socket()
    s.connect((host, port))
    s.send("hello " + str(i))
    print s.recv(1024)
    s.close()
