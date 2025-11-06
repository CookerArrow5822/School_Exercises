#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

i = 1
smallest = 0
while i < len(a) and s == "end":
    if int(a[i]) < int(a[smallest]):
        smallest = i

    i = i + 1

print(smallest)
