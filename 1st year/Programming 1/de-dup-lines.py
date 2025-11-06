#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    a.append(s)
    j = 0
    found = 0
    while j < len(a):
        if s == a[j]:
            found = 1
        if found == 1:
            

        j = j + 1
    s = input()