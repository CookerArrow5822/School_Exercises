#!/usr/bin/env python3

import sys

capacity = int(sys.stdin.readline().strip())

people = 0
dismissed = 0





for line in sys.stdin:
    line = line.strip()
    instruction, number = line.split()
    number = int(number)

    if instruction == "enter":
        temp = people + number
        if temp <= capacity:
            people = temp

        else:
            dismissed = dismissed + 1
    
    elif instruction == "leave":
        people = people - number


print(dismissed)
