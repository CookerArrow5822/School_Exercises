#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
    line = line.replace("m", "M", 1)
    print(line)
    i = i + 1
