#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
numbers = []

for num in lines:
    num = int(num.strip())
    multiple_3 = []
    multiple_3_squared = []
    multiple_4 = []
    multiple_4_doubled = []
    multiple_either = []
    multiple_both = []
    numbers = []
    for i in range(1, int(num)+ 1):
        numbers.append(i)

    multiple_3 = [n for n in numbers if n % 3 == 0]
    multiple_3_squared = [n * n for n in multiple_3]
    multiple_4 = [n for n in numbers if n % 4 == 0]
    multiple_4_doubled = [n * 2 for n in multiple_4]
    multiple_either = list(set(n for n in multiple_3 + multiple_4))

    multiple_either.sort()
    multiple_both = [n for n in multiple_3 if n in multiple_4]

    print("Multiples of 3:", multiple_3)
    print("Multiples of 3 squared:", multiple_3_squared)
    print("Multiples of 4 doubled:", multiple_4_doubled)
    print("Multiples of 3 or 4:", multiple_either)
    print("Multiples of 3 and 4:", multiple_both)
