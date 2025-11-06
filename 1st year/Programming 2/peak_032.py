#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

grid = [[int(num) for num in line.strip().split()] for line in lines]

M = len(grid)
N = len(grid[0]) if M > 0 else 0

for i in range(1, M - 1):
    for j in range(1, N - 1):
        value = grid[i][j]
        
        left = grid[i][j - 1]
        right = grid[i][j + 1]
        above = grid[i - 1][j]
        below = grid[i + 1][j]
        
        if value > left and value > right and value > above and value > below:
            print(value)
            sys.exit(0) 

print(-1)
