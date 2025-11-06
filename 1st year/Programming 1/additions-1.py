#!/usr/bin/env python3

i = 0
a = 10
while i < a:
    s = input()
    j = 0
    while s[j] != "+":
        j = j + 1

    num1 = s[0:j]
    num2 = s[j + 1:]
    total = int(num1) + int(num2)
    print(total)
    i = i + 1
