#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, sid, module_res):
        self.name = name
        self.sid = sid
        self.module_res = dict(module_res)

    def average_mark(self):
        return round(sum(self.module_res.values()) / len(self.module_res))
    
    def __str__(self):
        sorted_modules = sorted(self.module_res.keys())
        modules_str = ", ".join(sorted_modules)
        return (f"Name: {self.name}\n"
                f"ID: {self.sid}\n"
                f"Modules: {modules_str}\n"
                f"Average mark: {self.average_mark()}")
    
class Classlist(object):

    def __init__(self):
        self.students = {}

    def add(self, student):
        self.students[student.sid] = student

    def sort_by_average(self, student):
        return student.average_mark()

    def __str__(self):
        sorted_students = sorted(self.students.values(), key=self.sort_by_average, reverse=True)
        return "\n".join(str(student) for student in sorted_students)
