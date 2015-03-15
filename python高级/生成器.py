'getNum是生成器函数'
def getNum():
    yield 1
    yield 2
    yield 3

'调用生成器函数将返回一个生成器'
generator = getNum()

'''
第一次调用生成器的next方法时，生成器开始执行生成器函数（而不是构建生成器时）
直到遇到yield时暂停执行（挂起）
并且yield的参数将作为此次next方法的返回值
'''
print generator.next()

'''
之后每次调用生成器的next方法，生成器将从上次暂停执行的位置恢复执行生成器函数
直到再次遇到yield时暂停，并且同样的，yield的参数将作为next方法的返回值
'''
print generator.next()
print generator.next()

'''
如果当调用next方法时生成器函数结束
则这次next方法的调用将抛出StopIteration异常
'''
print generator.next()
