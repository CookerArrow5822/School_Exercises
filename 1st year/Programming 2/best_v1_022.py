#!/usr/bin/env python3

import sys

fileName = sys.argv[1]

names = []
grades = []


with open(fileName, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        name = "".join(char for char in line if not char.isdigit()).strip()
        names.append(name)
        grade = "".join(n for n in line if n.isdigit())
        grades.append(grade)
    

    highest = max(grades)
    index_highest = grades.index(highest)

    print("Best student:", names[index_highest])
    print("Best mark:", grades[index_highest])




