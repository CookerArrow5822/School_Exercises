#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    matches = re.finditer(r"([a-z])\1*", line.strip())  
    compressed = [f"{len(m[0])}{m[0][0]}" for m in matches]  
    print("".join(compressed))
