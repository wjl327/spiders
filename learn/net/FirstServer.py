__author__ = 'Jarvis.Wu'

import socket

host = "localhost"
port = 12345

s = socket.socket()
s.bind((host, port))
s.listen(5)

print "My Server started"

while True:
    client, addr = s.accept()
    print "Got connection from",addr
    print "Got message is :",client.recv(1024)
    client.send("Thank you " + str(addr) + " for connecting")
    client.close()