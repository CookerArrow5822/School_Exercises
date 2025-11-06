#!/usr/bin/env python3

import sys

vowels = "aeiou"
output = []
for line in sys.stdin:
    line = line.strip()
    i = 0
    decoded = []
    while i < len(line):
        if line[i] in vowels:
            decoded.append(line[i])
            i = i + 2
        else:
            decoded.append(line[i])
        
        i = i + 1
    
    output.append("".join(decoded))

for i in range(len(output)):
    print(output[i])
