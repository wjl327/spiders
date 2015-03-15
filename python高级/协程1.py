import time

def coroutine(func):
    f = func()
    f.next()
    return f

def consumer():
    print "Wait to getting a task"
    while 1:
        n = (yield n)
        print "Got", n

def producer():
    c = coroutine(consumer)
    while 1 :
        time.sleep(1);
        print "send a task to consumer()"
        c.send("task")

if __name__ == "__main__" :
    producer()
