#!/usr/bin/env python3

import sys
words = sys.stdin.read().split
sentence = ""
i = 0
while words[i] != "end":

    while words[i] != " ":

        if words[i] == ".":
            print(sentence)
            sentence = ""
        else:
            sentence = sentence + words[i]
            sentence = sentence + " "
        i = i + 1
