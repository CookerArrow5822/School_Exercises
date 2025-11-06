#!/usr/bin/env python3

import sys

line = sys.stdin.read().strip()
line = line.split(";")
questions = 0
for num in line:
    if "-" in num:
        M, N = num.split("-")
        questions = questions + (int(N) - int(M)) + 1

    else:
        questions += 1

print(questions)