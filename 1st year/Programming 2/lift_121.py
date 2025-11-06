#!/usr/bin/env python3

import sys

def solve():
    line = sys.stdin.readline().split()
    f = int(line[0])
    s = int(line[1])
    g = int(line[2])
    u = int(line[3])
    d = int(line[4])

    if s == g:
        print(0)
        return

    queue = [(s, 0)]
    visited = {s}
    head = 0

    while head < len(queue):
        current_floor, steps = queue[head]
        head += 1

        next_floor_up = current_floor + u
        if 1 <= next_floor_up <= f and next_floor_up not in visited:
            if next_floor_up == g:
                print(steps + 1)
                return
            visited.add(next_floor_up)
            queue.append((next_floor_up, steps + 1))

        next_floor_down = current_floor - d
        if 1 <= next_floor_down <= f and next_floor_down not in visited:
            if next_floor_down == g:
                print(steps + 1)
                return
            visited.add(next_floor_down)
            queue.append((next_floor_down, steps + 1))

    print("Sorry Sheila!")

if __name__ == "__main__":
    solve()
    