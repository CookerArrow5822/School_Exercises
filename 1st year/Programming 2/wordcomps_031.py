#!/usr/bin/env

import sys

lines = sys.stdin.readlines()
words = []

for line in lines:
    line = line.strip()
    words.append(line)

letters_17 = [n for n in words if len(n) == 17]
letters_18 = [n for n in words if len(n) >= 18]
letters_a = [word for word in words if word.lower().count("a") == 4]
letters_q = [n for n in words if n.lower().count("q") >= 2]
sequence_cie = [n for n in words if "cie" in n]
anagram_angle = [n for n in words if n != "angle" and len(n) == 5 and n.lower().count("a") == 1 and n.lower().count("n") == 1 and n.lower().count("g") == 1 and n.lower().count("l") == 1 and n.lower().count("e") == 1 ]

print("Words containing 17 letters:", letters_17)
print("Words containing 18+ letters:", letters_18)
print("Words with 4 a's:", letters_a)
print("Words with 2+ q's:", letters_q)
print("Words containing cie:", sequence_cie)
print("Anagrams of angle:", anagram_angle)