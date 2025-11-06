#!/usr/bin/env python3

class Element(object):

    def set_attributes(element, number, name, symbol, bp):
        element.number = number
        element.name = name
        element.symbol = symbol
        element.bp = bp

    def print_attributes(element):
        print(f"Number: {element.number}")
        print(f"Name: {element.name}")
        print(f"Symbol: {element.symbol}")
        print(f"Boiling point: {element.bp} K")