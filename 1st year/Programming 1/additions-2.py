#!/usr/bin/env python3

i = 0
total = 0
s = input()
j = 0
while i != 5:
    o = j
    while j < len(s) and s[j] != "+":
        j = j + 1
    num = int(s[o:j])
    j = j + 1
    total = total + num
    i = i + 1

print(total)
