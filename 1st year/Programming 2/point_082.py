#!/usr/bin/env python3

import math

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.x - other.y) ** 2)
    
    def __str__(self):
        return(f"({self.x}, {self.y})")
