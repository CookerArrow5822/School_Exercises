#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def midpoint(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2

        return Point(x, y)
    
    def distance(self, other):
        distance = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return distance
    
    def __str__(self):
        return(f"({self.x}, {self.y})")
    
class Circle(object):

    def __init__(self, centre=None, radius=1):
        if centre == None:
            self.centre = Point(0, 0)
        else:
            self.centre = centre
        
        self.radius = radius

    def __str__(self):
        return f"Centre: {self.centre}\nRadius: {self.radius}"