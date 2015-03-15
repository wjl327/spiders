#coding=utf8

def fun1(*args):
    print args


def fun2(**kwargs):
    print kwargs
    print kwargs['arg1'],kwargs['arg2']

def fun3(*args, **kwargs):
    print args,kwargs


if __name__ == "__main__" :
    fun1(1, 'a', "abc");
    fun1(*['a', 'b', 'c'])
    fun2(**{'arg1': '1', 'arg2': 'two', 'arg3': None})
    fun3(*('A', 'B', 'C'), **{"name":"JarvisWu", "age":25})
