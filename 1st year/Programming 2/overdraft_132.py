#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
balance = 0
min_balance = 0

for line in lines:
    amount = int(line.strip())

    balance = balance + amount
    
    if balance < min_balance:
        min_balance = balance

print(abs(min_balance))