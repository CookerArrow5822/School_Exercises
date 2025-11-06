#!/usr/bin/env python3

import sys


num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    
for line in sys.stdin:
    numbers = map(int, line.split())
    words = [num_words[num] for num in numbers]
    print(" ".join(words))

