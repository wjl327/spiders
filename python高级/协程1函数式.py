import time

def coroutine(func):
    def ref():
        f = func()
        f.next()
        return f
    return ref

@coroutine
def consumer():
    print "Wait to getting a task"
    while 1:
        n = (yield)
        print "Got", n

def producer():
    c = consumer()
    while 1 :
        time.sleep(1);
        print "send a task to consumer()"
        c.send("task")

if __name__ == "__main__" :
    producer()
