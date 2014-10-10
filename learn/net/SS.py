__author__ = 'Administrator'

import socket,select,time

server = socket.socket()
server.bind(("localhost", 1234))
server.listen(5)

inputs = [server]
outputs = []
exceptions = []

while True:
    print "waiting for next event"
    readable , writable , exceptional = select.select(inputs, outputs, exceptions)
    for r in readable:
        if r is server:
            client, addr = server.accept()
            print 'Got connection from', addr
            inputs.append(client)
    else:
        try:
            data = r.recv(1024)
            disconnected = not data
        except socket.error:
            disconnected = True

        if disconnected:
            print "disconnected status is :",disconnected
        else:
            print data
