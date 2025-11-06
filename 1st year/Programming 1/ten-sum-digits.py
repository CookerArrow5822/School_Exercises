#!/usr/bin/env python3

i = 0
a = 10
total = 0

while i < a:
    s = int(input())
    if s > 0:
        s = s % 10
        total = total + s

    else:
        s = s % 10
        if s == 0:
            s = s
        else:
            s = 10 - s
            total = total + s
    i = i + 1

print(total)
