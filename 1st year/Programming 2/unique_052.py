#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = [int(num) for num in line.strip().split()]

    if len(line) == 0:
        print("none")
        continue


    while True and len(line) >= 1:
        max_line_value = max(line)
        if line.count(max_line_value) >= 2:
            line = [num for num in line if num!= max_line_value]
        
        else:
            break

    if len(line) == 0:
        print("none")
    else:
        print(max(line))