#!/usr/bin/env python3

def reverse(numbers):
    if len(numbers) == 1:
        return [1]
    
    else:
        reverse_list = numbers[::-1]
        return reverse_list