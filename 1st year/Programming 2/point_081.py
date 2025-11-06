#!/usr/bin/env python3

class Point(object):

    def set_attributes(point, x, y):
        point.x = float(x)
        point.y = float(y)

    def print_attributes(point):
        print(f"x: {point.x}0")
        print(f"y: {point.y}0")

    def reflect(point):
        point.x = point.x * -1
        point.y = point.y * -1