__author__ = 'Jarvis.Wu'

class Student:

    def __init__(self, _id, _name, _teacher, _sex="male"):
        self.id = _id
        self.name = _name
        self.sex = _sex
        self.teacher = _teacher

    def __str__(self):
        return "Student [id = " + str(self.id) + " name = " + self.name + " sex = " + self.sex + " the teacher is " \
               + str(self.teacher) + " ]"