#!/usr/bin/env python3

def histogram(numbers, character):
    for number in numbers:
        print(character * number)

histogram([6, 2, 15, 3, 20, 5],"=")
    