#!/usr/bin/env python3

s = input()
here = 0
while s != "end":
    first = s[0]
    second = s[1]
    if first == second and here != 1:
        num = s
        here = 1
    s = input()
if here == 1:
    print(num)
