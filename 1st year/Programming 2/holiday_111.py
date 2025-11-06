#!/usr/bin/env python3

import sys

def find_best_departure(temperatures):
    min_max_temp = float('inf')
    best_day = 0
    
    for k in range(len(temperatures) - 2):
        current_max = max(temperatures[k], temperatures[k+2])
        if current_max < min_max_temp or (current_max == min_max_temp and k < best_day):
            min_max_temp = current_max
            best_day = k
    
    return best_day + 1, min_max_temp

def main():
    temps = list(map(int, sys.stdin.readline().split()))
    if len(temps) < 3:
        print(1, max(temps))
        return
    day, temp = find_best_departure(temps)
    print(day, temp)

if __name__ == '__main__':
    main()