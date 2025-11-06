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

    def service(self):
        
        if self.mileage == 0:
            return f"Service due in {10000} mile(s)"


        elif self.mileage % 10000 != 0:
            return f"Service due in {10000 - self.mileage % 10000} mile(s)"
        
        else:
            return f"Service due now"

    def __str__(self):
        str_drivers = ", ".join(self.drivers)
        return f"Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {str_drivers}\n{self.service()}"