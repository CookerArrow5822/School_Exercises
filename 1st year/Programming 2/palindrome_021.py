#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip().lower()
    line = line.replace(" ", "")
    line = line.replace(".", "")
    line = line.replace(",", "")
    line = line.replace(":", "")
    line = line.replace("?", "")
    reverse_line = line[::-1]

    if line == reverse_line:
        print("True")
    else:
        print("False")
    
    i = i + 1