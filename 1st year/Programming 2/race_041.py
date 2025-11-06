#!/usr/bin/env python3

import sys

runner = ""
best = 0

for line in sys.stdin:
    tokens = line.split()
    name = tokens[0]
    times = tokens[1:]

    for time in times:
        if not time.replace(":", "").isdigit():
            break

        minutes, seconds = map(int, time.split(":"))
        total_seconds = minutes * 60 + seconds

        if best == 0 or total_seconds < best:
            best = total_seconds
            runner = name
            best_time = time

print(f'{runner}: {best_time}')