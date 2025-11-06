#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()




line = lines[0].strip().split()
numbers = [int(n) for n in line if n.isdigit()]


line = lines[1].strip().split()
letters = [c.upper() for c in line if c.isalpha()]

get_letters = letters[0]
letters = [c for c in get_letters if c.isalpha()]


maxnum = int(max(numbers))
numbers.remove(maxnum)
minnum = int(min(numbers))
numbers.remove(minnum)
midnum = int(numbers[0])

print_list = []

i = 0
while i < len(letters):
    if letters[i] == "A":
        print_list.append(minnum)
    elif letters[i] == "B":
        print_list.append(midnum)
    else:
        print_list.append(maxnum)
    i = i + 1


print(print_list[0], print_list[1], print_list[2])

        
    


# import sys
# seperate both lines
# seperate the numbers
# add numbers to list
# seperate the letters
# add letters to list
# find the minimum and assign it to A
# find the maximum and assign it to C
# the other number gets assigned to B
# reads letters list and based on what it reads print out the appropriate result