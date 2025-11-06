#!/usr/bin/env python3

import sys

game = sys.stdin.read().splitlines()
number = []
status = []

for line in game:
    if line.isdigit():
        number.append(int(line))
    elif line != "correct":
        status.append(line)

i = 0
while i < len(status):
    if number[i] < number[i + 1] and status[i] == "higher":
        i = i + 1
    elif number[i] > number[i + 1] and status[i] == "lower":
        i = i + 1
    else:
        print("Bert is not to be trusted")
        break
else:
    print("Bert can be trusted")