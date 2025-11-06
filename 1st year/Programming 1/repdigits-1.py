#!/usr/bin/env python3

n = int(input())
i = 0
while i < n:
    s = input()
    if len(s) > 1:
        first = s[0]
        second = s[1]
        if first == second:
            print(s)

    i = i + 1
