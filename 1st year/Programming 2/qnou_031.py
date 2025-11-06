#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

words = []

for line in lines:
    line = line.strip()
    words.append(line)

q_no_u = [
    word for word in words
        if any(word.lower()[i] == "q" and (i == len(word) - 1 or word.lower()[i+1] != "u")
               for i in range(len(word)))
               ]
print("Words with q but no u:", q_no_u)