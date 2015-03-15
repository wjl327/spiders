'''
利用了python生成器知识
生成器其实也就是迭代器
'''
def repeater():
    n = 0
    while True:
        n= (yield n)


'''
send是除next外另一个恢复生成器的方法。
Python 2.5中，yield语句变成了yield表达式，这意味着yield现在可以有一个值。
而这个值就是在生成器的send方法被调用从而恢复执行时，调用send方法的参数。
调用send传入非None值前，生成器必须处于挂起状态，否则将抛出异常。
所以这里先调用next()让线程执行和挂起
'''
r = repeater()

print r.next()
print r.send(10)

#close方法用于关闭生成器。对关闭的生成器后再次调用next或send将抛出StopIteration异常
r.close()

