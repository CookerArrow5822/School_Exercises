#!/usr/bin/env python3

class Memories(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def remember(self, key):
        return getattr(self, key, "False")



person1 = Memories(name='Tom', age=32, salary=50000)

print (person1.remember("salary"))
print (person1.remember("email"))




# initialise pers 1 details
# define remember using getattr to get attribute
# make it use entered remember value and error string False
# print answers