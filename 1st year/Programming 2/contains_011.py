#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0

while i < len(lines):
    left, right = lines[i].strip().lower().split()
    state = True
    for c in left:
        if c not in right:
            state = False
            break

        right = right.replace(c, "", 1)
    if state == True:
        print("True")
    else:
        print("False")

    i = i + 1
