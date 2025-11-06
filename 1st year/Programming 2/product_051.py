#!/usr/bin/env python3

import sys

value = sys.stdin.readline().strip()
done = False

def get_ranged_digit(value):
    value_range = "123456789"
    if value in value_range:
        return(value)

    while True:
        numbers = [int(num) for num in value if num != "0"]
        number = 1
        for num in numbers:
            number = number * num

        value = str(number)
        if value in value_range:
            return(value)



number = get_ranged_digit(value)
print(number)

