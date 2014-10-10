import threading,time

#线程PrintThread继承于threading.Thread!!并且覆盖run方法
class PrintThread(threading.Thread):
	def __init__(self, name = None):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		for i in range(5):
			time.sleep(1)
			print self.name

def test():
	for i in range(0, 3):
		t = PrintThread("t"+str(i))
		t.start()

if __name__ == '__main__':
	test()