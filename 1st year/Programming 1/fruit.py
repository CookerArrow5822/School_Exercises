#!/usr/bin/env python3

import sys
words = sys.stdin.read().split()

fruits = {
    "apple": True,
    "cherry": True,
    "pear": True,
    "banana": True,
    "orange": True,
}

i = 0
while i < len(words):
    word = words[i]
    if word in fruits:
        print(word)
    i = i + 1
