#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

def endings(line):
    length = len(line)
    if line[-2:] == "ch" or line[-2:] == "sh":
        line = line + "es"
        return line
    elif line[-1] == "x" or line[-1] == "s" or line[-1] == "z":
        line = line + "es"
        return line
    elif line[-1] == "f":
        line = line[0:length - 1]
        line = line + "ves"
        return line
    elif line[-2:] == "fe":
        line = line[0:length - 2]
        line = line + "ves"
        return line
    elif line[-1] == "o":
        line = line + "es"
        return line
    elif line[-2] not in "aeiou" and line[-1] == "y":
        line = line[0:length - 1]
        line = line + "ies"
        return line
    else:
        line = line + "s"
        return line


i = 0 
while i < len(lines):
    line = lines[i].strip()
    plural = endings(line)
    print(plural)
    i = i + 1