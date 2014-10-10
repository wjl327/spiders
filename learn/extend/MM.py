__metaclass__ = type
__author__ = 'Jarvis.Wu'

class Bird:

    def __init__(self):
        print "Bird init..."
        self.hungry = True

    def eat(self):
        if self.hungry :
            print "Aaaaah...."
            self.hungry = False
        else:
            print "No,thanks"

class SongBird(Bird):

    def __init__(self):
        super(SongBird, self).__init__()
        print "SongBird init..."
        self.sound = "Squawk!"

    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()