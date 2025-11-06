#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
    if int(len(line)) % 2 == 0:
        print("No middle character!")
    else:
        mid = int(len(line))
        mid = mid // 2
        print(line[mid])
    i = i + 1
