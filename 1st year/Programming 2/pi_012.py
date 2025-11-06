#!/usr/bin/env python3

import sys
from math import pi

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = int(lines[i])
    print(f"{pi:.{line}f}")
    i = i + 1