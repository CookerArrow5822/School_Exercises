#!/usr/bin/env python3

import sys


def digit(line):
    global digits
    for c in line:
        if c.isdigit():
            digits = 1
            return(digits)

def lower(line):
    global lowers
    for c in line:
        if c.islower():
            lowers = 1
            return(lowers)

def upper(line):
    global uppers
    for c in line:
        if c.isupper():
            uppers = 1
            return(uppers)

def special(line):
    global specials
    for c in line:
        if not c.isalnum() and not c.isspace():
            specials = 1
            return(specials)
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    char = 0
    digits = 0
    lowers = 0
    uppers = 0
    specials = 0
    line = lines[i].strip()
    digit(line)
    lower(line)
    upper(line)
    special(line)
    char = digits + lowers + uppers + specials
    print(char)
    i = i + 1