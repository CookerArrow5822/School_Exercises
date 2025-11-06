#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
j = 0
while i < len(lines):
    line = lines[i]
    first = "a"
    second = "b"
    while j < len(line):
        if line[j] == " ":
            first = line[0:j].upper()
            second = line[j+1:].upper()
            j = j + 1
        else:
            j = j + 1
    if first in second:
        print("True")
    else:
        print("False")

    i = i + 1
    j = 0
