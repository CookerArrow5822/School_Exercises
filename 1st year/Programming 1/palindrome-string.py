#!/usr/bin/env python3

s = input()
i = 0
num = len(s)
while s[i] == s[num - i - 1]:
    i = i + 1

if i == len(s):
    print("palindrome")