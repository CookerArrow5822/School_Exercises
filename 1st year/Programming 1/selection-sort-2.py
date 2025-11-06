#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

start = int(input())
i = start
smallest = i
while i < len(a):
    if int(a[i]) < int(a[smallest]):
        smallest = i

    i = i + 1

print(smallest)
