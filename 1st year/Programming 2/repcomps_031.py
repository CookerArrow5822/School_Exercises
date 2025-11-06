#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
numbers = []

for num in lines:
    num = int(num.strip())
    numbers = []
    for i in range(1, int(num)+ 1):
        numbers.append(i)
    multiple_3 = []
    multiple_3 = [i if (i % 3 == 0) else 0 for i in numbers]
    print("Non-multiples of 3 replaced:", multiple_3)
