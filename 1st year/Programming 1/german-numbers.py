#!/usr/bin/env python3

import sys
word = sys.stdin.read().split()
dictionary = {}

english = "zero one two three four five six seven eight nine ten".split()
german = "null eins zwei drei vier funf sechs sieben acht neun zehn".split()

i = 0
while i < len(english):
    dictionary[english[i]] = german[i]
    i = i + 1

j = 0
while j < len(word):
    if word[j] in dictionary:
        print(dictionary[word[j]])
    j = j + 1
