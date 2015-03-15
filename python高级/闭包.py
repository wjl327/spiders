def f():
    x = 1
    def inner():
        print x
    inner()
    x = 2
    inner()

if __name__ == '__main__' :
    f()
