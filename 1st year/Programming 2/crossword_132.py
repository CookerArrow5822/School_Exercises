#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
vertical_word = []
horizontal_word = ""

line = lines[0]
i = 0

while i < len(line):
    if i != ".":
        x = i
        print(line.split())
        if line.split().count(i) >= 2:
            horizontal_word = line
            print("all good")

    i = i + 1

for line in lines:
    vertical_word.append(line[x])

print(horizontal_word)
print(vertical_word)


print(f'{horizontal_word} {"".join(vertical_word)}')