import sys

lines = sys.stdin.readlines()

i = 0
while (i < len(lines)):
    line = lines[i].strip()
    chopped = line[1:len(line) - 1]
    if chopped:
        print(chopped)
    i = i + 1
