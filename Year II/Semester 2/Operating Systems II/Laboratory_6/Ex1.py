import random

class Factor(object):
    def __init__(self, id, name, status, time):
        self.id = id
        self.name = name
        self.status = status
        self.time = time
    
    def show(self):
        print("id: " + str(self.id) + ", name: " + str(self.name) +
        ", status: " + str(self.status) + ", time: " + str(self.time))

class Person(Factor):
    def __init__(self, habit, location):
        self.disease = None
        self.habit = habit
        self.location = location
    
    def