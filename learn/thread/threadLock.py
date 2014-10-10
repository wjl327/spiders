import thread,time

count = 0

lock = thread.allocate_lock() 
def increment():
	global count;
	lock.acquire()
	for i in range(10000):
		count+=1
	lock.release()

for i in range(10):
	thread.start_new_thread(increment, ())

time.sleep(5)
print count