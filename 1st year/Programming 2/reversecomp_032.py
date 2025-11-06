#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

# Binary search (adapted from CSC1003)
def binsearch(query, sorted_list):
    '''Return True if query in sorted_list otherwise False.'''
    
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True  # Found it

    return False  # Not found

# Store original words while maintaining a sorted lowercase version for binary search
words = [line.strip() for line in lines]
words_lower = sorted(word.lower() for word in words)

# Find words that have a reversed match in the list (ignoring case)
reverse_words = [word for word in words 
                 if len(word) >= 5 and binsearch(word[::-1].lower(), words_lower)
                    ]

print(reverse_words)
