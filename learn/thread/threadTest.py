#coding:utf-8
import thread,time

def hello(i = ''):
	print 'hello' + str(i)

def test1():
	for i in range(5):
		thread.start_new_thread(hello, ())

def test2():
	for i in range(5):
		thread.start_new_thread(hello, (i,))

#采用thread模块start_new_thread启动子线程，主线程必须等到子线程结束
if __name__ == '__main__':
	test1()
	time.sleep(1)
	test2()
	time.sleep(1)
