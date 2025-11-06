#!/usr/bin/env python3

s = input()
i = 0
last_digit = ""
while i < len(s):
    if s[i] >= "0" and s[i] <= "9":
        last_digit = s[i]
    i = i + 1
if len(last_digit) != 0:
    print(last_digit)
