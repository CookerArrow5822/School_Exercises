#!/usr/bin/env python3

import sys
import string

def count_frequency():
    word_counts = {}

    for line in sys.stdin:
        line = line.lower()
        line = "".join([char for char in line if char == "'" or char not in string.punctuation])
        words = line.split()
        words = sorted(words)

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return(word_counts)

word_count = count_frequency()
for word in sorted(word_count):
    print(f'{word}: {word_count[word]}')