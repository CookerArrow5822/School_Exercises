#!/usr/bin/env python3

import sys


def count_e(line):
    count = 0
    line = line.strip()
    if "e" in line:
        count = line.count("e")
    return(count)
    
def hey(count):
    count = count * 2
    word = "h"+"e"*count+"y"
    return(word)


for line in sys.stdin:
    count = count_e(line)
    if count >= 1:
        word = hey(count)
    
    print(word)
