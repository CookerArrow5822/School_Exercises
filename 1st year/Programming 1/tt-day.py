#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

num = int(input())
i = 0
while i < len(a):
    s = a[i]
    toks = s.split()
    if int(toks[0]) == num:
        print(s)
    i = i + 1
