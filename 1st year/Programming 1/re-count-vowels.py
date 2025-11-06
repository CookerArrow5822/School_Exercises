#!/usr/bin/env python3

import sys
s = sys.stdin.read()

vowel = 0
i = 0
vowels = "aeiouAEIOU"

while i < len(s):
    if s[i] in vowels:
        vowel = vowel + 1

    i = i + 1

print(vowel)
