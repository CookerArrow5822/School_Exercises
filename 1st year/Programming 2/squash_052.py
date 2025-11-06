#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    result = ""
    count = 1

    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            count += 1
        else:
            result += str(count) + line[i - 1]
            count = 1

    if line:
        result += str(count) + line[-1]

    print(result)
