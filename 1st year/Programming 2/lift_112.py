#!/usr/bin/env python3

def lift_112():
    f, s, g, u, d = [int(x) for x in input().split()]

    if s == g:
        print(0)
        return

    queue = [(s, 0)]
    visited = [False] * (f + 1)
    visited[s] = True

    front = 0
    while front < len(queue):
        current_floor, presses = queue[front]
        front += 1

        if u > 0:
            next_floor_up = current_floor + u
            if next_floor_up <= f and not visited[next_floor_up]:
                if next_floor_up == g:
                    print(presses + 1)
                    return
                visited[next_floor_up] = True
                queue.append((next_floor_up, presses + 1))

        if d > 0:
            next_floor_down = current_floor - d
            if next_floor_down >= 1 and not visited[next_floor_down]:
                if next_floor_down == g:
                    print(presses + 1)
                    return
                visited[next_floor_down] = True
                queue.append((next_floor_down, presses + 1))

    print("Sorry Sheila!")

if __name__ == "__main__":
    lift_112()
