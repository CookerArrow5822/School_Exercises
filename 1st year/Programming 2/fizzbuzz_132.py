#!/usr/bin/env python3

import sys

line = sys.stdin.readline()
line = line.strip().split()

x = int(line[0])
y = int(line[1])
N = int(line[2])

for num in range (1, N + 1):
    if num % x == 0 and num % y == 0:
        print("fizzbuzz")
    
    elif num % x == 0:
        print("fizz")

    elif num % y == 0:
        print("buzz")
    
    else:
        print(num)