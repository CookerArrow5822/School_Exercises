#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while (i < len(lines)):
    line = lines[i].strip()
    line = line.capitalize()
    line = line[:-1] + line[-1].upper()

    print(line)
    i = i + 1
