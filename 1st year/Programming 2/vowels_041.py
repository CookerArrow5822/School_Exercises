#!/usr/bin/env python3

import sys
import string

def count_vowels():
    number_vowels = {}
    vowels = "aeiou"

    for vowel in vowels:
        number_vowels[vowel] = 0

    for line in sys.stdin:
        line = line.lower()
        for char in line:
            if char in vowels:
                number_vowels[char] += 1
        
    return(number_vowels)

vowel_count = count_vowels()
sorted_vowel_count = sorted(vowel_count.items(), key=lambda item: item[1], reverse=True)
width = len(str(sorted_vowel_count[0][1]))

for vowel, count in sorted_vowel_count:
    print(f'{vowel}: {count:>{width}}')
