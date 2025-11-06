#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()



line = lines[0].strip()

k = 0


while k < len(line) and line[k].isdigit():
    k = k + 1

bucket = int(line[:k])

fills = 0

for i in range(1, len(lines)):
    line = lines[i].strip().split()
    j = 0

    while j < len(line) and bucket >= 0:
        bucket = bucket - int(line[j])
        if bucket >= 0:
            fills = fills + 1
        
        j = j + 1

print(fills)