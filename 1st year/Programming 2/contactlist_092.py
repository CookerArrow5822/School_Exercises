#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.phone} {self.email}"

class Contactlist(object):

    def __init__(self, d=None):
        if d is None:
            self.d = {}
        else:
            self.d = d

    def add(self, c):
        self.d[c.name] = c 

    def remove(self, name):
        if name in self.d:
            del self.d[name]

    def get(self, name):
        if name in self.d:    
            return self.d[name]
        else:
            return None
    
    def __str__(self):
        output = []
        output.append("Contact list")
        output.append("------------")
        for k, v in sorted(self.d.items()):
            output.append('{}'.format(v))
        return '\n'.join(output)