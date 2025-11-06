#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
numbers = []

for num in lines:
    num = int(num.strip())
    numbers = []
    for i in range(1, int(num)+ 1):
        numbers.append(i)
    prime = []
    prime = [i for i in numbers if i == 2 or i == 3 or i == 5 or i == 7 or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0)]
    prime.remove(1)
    print("Primes:", prime)

