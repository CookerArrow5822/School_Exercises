#!/usr/bin/env python3

class Customer(object):

    def __init__(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance

    def lodge(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return self.balance
        
        else:
            self.balance -= amount
            return self.balance

    def __str__(self):
        return f"Name: {self.name}\nNumber: {self.number}\nBalance: {self.balance:.2f}"