__author__ = 'Jarvis.Wu'

class Teacher:

    def __init__(self, _id, _name, _sex="male"):
        self.id = _id
        self.name = _name
        self.sex = _sex

    def __str__(self):
        return "Teacher [id = " + str(self.id) + " name = " + self.name + " sex = " + self.sex + "]"
