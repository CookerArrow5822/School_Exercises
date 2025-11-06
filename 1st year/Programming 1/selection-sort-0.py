#!/usr/bin/env python3

s = input()
smallest = 100000000
while s != "end":
    if smallest > int(s):
        smallest = int(s)
    else:
        smallest = smallest
    s = input()

print(smallest)
