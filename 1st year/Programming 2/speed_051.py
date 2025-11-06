#!/usr/bin/env python3

import sys

speed = []
total_speed = 0
previous_time = 0
previous_distance = 0

def calculate_speeds(time, distance, p_time, p_distance):
    time = int(current_time) - int(p_time)
    distance = int(current_distance) - int(p_distance)
    if time != 0 and distance != 0:
        speed = distance // time
    return(speed)

default_values = sys.stdin.readline().strip()

for line in sys.stdin:
    current_time, current_distance = line.strip().split()
    speed.append(calculate_speeds(int(current_time), int(current_distance), int(previous_time), int(previous_distance)))
    previous_distance = current_distance
    previous_time = current_time

max_speed = max(speed)
print(max_speed)