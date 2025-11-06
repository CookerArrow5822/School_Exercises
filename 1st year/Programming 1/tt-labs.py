#!/usr/bin/env python3

s = input()

while s != "end":
    toks = s.split()
    tok = toks[2]
    if int(tok) > 1:
        print(s)

    s = input()
