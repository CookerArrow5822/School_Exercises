#!/usr/bin/env python3

s = input()
i = 0
found = 0
if found != 2:
    while i < len(s) and not ("0" <= s[i] <= "9"):
        i = i + 1

    j = i
    while j < len(s) and s[j] != " ":
        j = j + 1

    if i < len(s) and found == 1:
        print(s[i:j], i)
    
    found = found + 1
