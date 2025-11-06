#!/usr/bin/env python3
import math
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def midpoint(self, x2, y2):
       x = (self.x + x2) / 2 
       y = (self.y + y2) / 2
       return Point(x, y)

    def distance(self, x2, y2):
        distance = math.sqrt((self.x - x2) ** 2 + (self.y - y2) ** 2)
        return distance

    def __str__(self):
        return f"{self.x}, {self.y}"
