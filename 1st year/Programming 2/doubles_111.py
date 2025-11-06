#!/usr/bin/env python3

import sys

words = [line.strip() for line in sys.stdin]

def count_double_vowels(word):
    vowels = "aeiou"
    double_vowel_count = 0
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i] == word[i + 1]:
            double_vowel_count += 1
            i += 2
        else:
            i += 1

    return double_vowel_count

def most_double_vowels(words):
    max_double_vowels = 0
    most_double_vowels_word = ""

    for word in words:
        double_vowels = count_double_vowels(word)
        if double_vowels > max_double_vowels:
            most_double_vowels_word = word
            max_double_vowels = double_vowels

    return most_double_vowels_word

print(most_double_vowels(words))
        