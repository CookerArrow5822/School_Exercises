#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
words = []
for line in lines:
    line = line.strip()
    words.append(line)

shortest = [w for w in words
            if ("a" in w.lower() and "e" in w.lower() and "i" in w.lower() and "o" in w.lower() and "u" in w.lower())]
shortest = min(shortest, key=len)
print("Shortest word containing all vowels:", shortest)

iary = [w for w in words
            if w.endswith("iary")]

print("Words ending in iary:", len(iary))


max_word_e = max([word.count("e") for word in words])
most_word_e = [word for word in words if word.count("e") == max_word_e]

print("Words with most e's:", most_word_e)