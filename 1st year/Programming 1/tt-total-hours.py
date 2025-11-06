#!/usr/bin/env python3

s = input()
total = 0
while s != "end":
    toks = s.split()
    toks = toks[2]
    total = total + int(toks)
    s = input()

print(total)
