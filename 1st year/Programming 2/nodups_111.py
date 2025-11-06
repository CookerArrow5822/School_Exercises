#!/usr/bin/env python3

import sys
import re

seen_words = []
for line in sys.stdin:
    words = line.split()
    result = []
    for word in words:

        match = re.match(r'^([a-zA-Z]*)([^a-zA-Z]*)$', word)
        if match:
            alphabetic_part = match.group(1)
            punctuation = match.group(2)
            lower_alphabetic = alphabetic_part.lower()

            if alphabetic_part:
                if lower_alphabetic in seen_words:

                    result.append("." + punctuation)
                else:
                    seen_words.append(lower_alphabetic)
                    result.append(word)
            else:
                result.append(word)
        else:
            result.append(word)
    print(" ".join(result))