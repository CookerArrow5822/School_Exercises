#!/usr/bin/env python3

import sys

def checker(first, second):
    i = 0
    if len(first) != len(second):
        return(False)
    while i < len(first):
        char = first[i]
        if char not in second:
            return(False)

        second = second.replace(char, "", 1)
        i = i + 1
        
    return(True)

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    
    line = lines[i].strip().split()

    first = line[0]
    second = line[1]

    state = checker(first, second)
    print(state)

    i = i + 1