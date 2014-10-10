#继承list实现，记录调用次数的List

class CountList(list):
    def __init__(self, *args):
        super(CountList, self).__init__(args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CountList, self).__getitem__(index)

cs = CountList(2,4,7)
cs[0]
cs[1]
print cs
print cs.counter