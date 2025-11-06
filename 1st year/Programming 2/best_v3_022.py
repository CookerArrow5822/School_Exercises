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
        grade = "".join(n for n in line if n.isdigit())

        if grade.isdigit():
            names.append(name)
            grades.append(int(grade))
        else:
            print(f"Invalid mark {grade} encountered. Skipping.")

# Find the highest mark
highest = max(grades)
# Find all students with the highest mark
best_students = [names[i] for i, grade in enumerate(grades) if grade == highest]

# Print output
print("Best student(s):", ", ".join(best_students))
print("Best mark:", highest)
