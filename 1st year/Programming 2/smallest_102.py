#!/usr/bin/env python3

def smallest(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    else:
        rest_smallest = smallest(numbers[1:])
        return numbers[0] if numbers[0] < rest_smallest else rest_smallest