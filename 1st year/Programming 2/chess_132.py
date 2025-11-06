#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

max_kings = 2
max_queens = 2
max_rooks = 4
max_bishops = 4
max_knights = 4
max_pawns = 16

for line in lines:
    output = []
    line = line.strip().split()

    output.append(str(max_kings - int(line[0])))
    output.append(str(max_queens - int(line[1])))
    output.append(str(max_rooks - int(line[2])))
    output.append(str(max_bishops - int(line[3])))
    output.append(str(max_knights - int(line[4])))
    output.append(str(max_pawns - int(line[5])))

    print(" ".join(output))