#!/usr/bin/env python3

class Vehicle(object):
    def __init__(self, reg, cat, mileage, drivers=None):
        self.reg = reg
        self.cat = cat
        self.mileage = mileage
        if drivers is None:
            self.drivers = []
        else:
            self.drivers = drivers

    def __str__(self):
        driver_str = ", ".join(self.drivers)
        return f"Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {driver_str}"

class Fleet:
    def __init__(self):
        self._vehicles = {}

    def add(self, vehicle):
        if vehicle.reg not in self._vehicles:
            self._vehicles[vehicle.reg] = vehicle

    def remove(self, reg_number):
        if reg_number in self._vehicles:
            del self._vehicles[reg_number]

    def lookup(self, reg_number):
        return self._vehicles.get(reg_number)

    def get_drivers_by_category(self, category):
        drivers = set()
        for vehicle in self._vehicles.values():
            if vehicle.cat == category:
                drivers.update(vehicle.drivers)
        return list(drivers)