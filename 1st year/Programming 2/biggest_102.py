#!/usr/bin/env python3

def biggest(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    else:
        rest_biggest = biggest(numbers[1:])
        return numbers[0] if numbers[0] > rest_biggest else rest_biggest