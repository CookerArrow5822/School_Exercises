#!/usr/bin/env python3

s = input()
i = 1
first = ""
second = ""
if len(s) != 1:
    first = s[i]
    second = s[i - 1]

    while i < len(s) and first != second:
        second = s[i - 1]
        first = s[i]
        i = i + 1

    total = first + second
    if i < len(s) or first == second:
        print(total)
