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
    
    def add_driver(self, driver):
        self.drivers.append(driver)

    

    def __str__(self):
        str_drivers = ", ".join(self.drivers)
        return f"Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {str_drivers}"