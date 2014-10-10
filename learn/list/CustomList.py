def checkIndex(key):
    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0:
        raise IndexError

class ArSequence:

    def __init__(self, start = 0, step = 1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

    def __delitem__(self, key):
        print "Delete key : " + str(key)

s = ArSequence(1,2)
for i in range(0, 10):
    print s[i],

print

s[4] = "B550"
s[5] = "hello"

for i in range(0, 10):
    print s[i],

print

try:
    s["aa"]
except TypeError:
    print "OMG......"