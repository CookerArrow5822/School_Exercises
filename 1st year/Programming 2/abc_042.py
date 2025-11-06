#!/usr/bin/env python3

import sys

numbers = list(map(int, sys.stdin.readline().split()))
order = sys.stdin.readline().strip()

sorted_numbers = sorted(numbers)

letter_map = {letter: num for letter, num in zip("ABCDEF", sorted_numbers)}

print(" ".join(str(letter_map[char]) for char in order))