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
    
class Bank(object):

    def __init__(self):
        self.customers = {}

    def add(self, customer):
        self.customers[customer.number] = customer

    def remove(self, number):
        if number in self.customers:
            del self.customers[number]

    def lookup(self, number):
        return self.customers.get(number)
    