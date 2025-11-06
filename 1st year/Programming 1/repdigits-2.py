#!/usr/bin/env python3

found = False
while found != 1:
    s = input()
    first = s[0]
    second = s[1]
    if first == second:
        found = 1

if found == 1:
    print(s)
