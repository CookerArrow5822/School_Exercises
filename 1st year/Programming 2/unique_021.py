#!/usr/bin/env python3

import sys
import string


text = sys.stdin.read().split()
count = 0
duplicate = []
for word in text:
    word = word.lower()
    for char in word:
        noPunctuation = ''.join(char for char in word if char not in string.punctuation)
    if noPunctuation not in duplicate:
        duplicate.append(noPunctuation)
        count = count + 1
print(count - 1)