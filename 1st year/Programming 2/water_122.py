#!/usr/bin/env python3

import sys

def solve():
    n = int(sys.stdin.readline())
    connections = []
    for line in sys.stdin:
        p, q = map(int, line.split())
        connections.append((p, q))

    has_water = [False] * (n + 1)
    has_water[1] = True

    updated = True
    while updated:
        updated = False
        for p, q in connections:
            if has_water[p] and not has_water[q]:
                has_water[q] = True
                updated = True
            if has_water[q] and not has_water[p]:
                has_water[p] = True
                updated = True

    no_water_supply = []
    for i in range(1, n + 1):
        if not has_water[i]:
            no_water_supply.append(i)

    print(no_water_supply)

if __name__ == "__main__":
    solve()