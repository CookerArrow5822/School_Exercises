#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    j = 0
    line = lines[i].strip()
    while not line[j].isdigit():
        j = j + 1
    
    name = line[0:j]
    name = name.replace(".", " ")
    k = 0
    while name[k] != " ":
        k = k + 1
    first_name = name[0:k]
    surname = name[k+1:]

    first_name = first_name.capitalize()
    surname = surname.capitalize()
    print(first_name + " " + surname)
    i = i + 1
