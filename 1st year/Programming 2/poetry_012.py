#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
largest = ""

i = 0

while i < len(lines):
    line = lines[i].strip()
    if len(line) > len(largest):
        largest = line
    i = i + 1
largest = len(largest)
i = 0
while i < len(lines):
    line = lines[i].strip()
    print(f"{line:^{largest}}")
    i = i + 1
