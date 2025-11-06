#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

xs = []
ys = []

for line in lines:
    line = line.strip().split()

    xs.append(line[0])
    ys.append(line[1])

for point in xs:
    if xs.count(point) == 1:
        x = point

for point in ys:
    if ys.count(point) == 1:
        y = point

print(f"{x} {y}")
