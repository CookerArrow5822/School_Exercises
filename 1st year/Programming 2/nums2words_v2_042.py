#!/usr/bin/env python3

import sys


def load_translation(fileName):
    translation = {}
    with open(fileName, "r") as file:
        for line in file:
            english, translated = line.strip().split()
            translation[english] = translated
    return translation

translation_file = sys.argv[1]
translation = load_translation(translation_file)

num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

for line in sys.stdin:
    numbers = map(int, line.split())
    words = [translation[num_words[num]] for num in numbers]
    print(" ".join(words))

