#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

hours = 0
minutes = 0

i = 0
while i < len(lines):
    line = lines[i].strip().split(":")
    hours = int(line[0])
    minutes = int(line[1])
    minutes = minutes - 47
    if minutes < 0:
        hours = hours - 1
        minutes = minutes + 60
    
    if minutes == 60:
        hours = hours + 1
        minutes = 0
    if hours < 0:
        hours = hours + 24
    
    print(f"{hours:0>2d}:{minutes:0>2d}")

    i = i + 1