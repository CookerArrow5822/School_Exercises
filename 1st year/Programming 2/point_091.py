#!/usr/bin/env python3
import math
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def midpoint(self, other):
       x = (self.x + other.x) / 2 
       y = (self.y + other.y) / 2
       return Point(x, y)

    def distance(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance

    def __str__(self):
        return f"{self.x}, {self.y}"
