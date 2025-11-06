#!/usr/bin/env python3

class Vehicle(object):

    def __init__(self, reg, cat, mileage, drivers=None):
        self.reg = reg
        self.cat = cat
        self.mileage = mileage
        if drivers == None:
            self.drivers = []
        
        else:
            self.drivers = drivers

    def __str__(self):
        self.drivers = ", ".join(self.drivers)
        return f"Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {self.drivers}"