#!/usr/bin/env python3

def find_missing_number(M, N, sequence_str):
    expected = set(map(str, range(M, N + 1)))
    given = set()
    i = 0
    n = len(sequence_str)
    while i < n:
        for l in range(1, 6):
            num_str = sequence_str[i:i+l]
            if num_str in expected and num_str not in given:
                given.add(num_str)
                i += l
                break
        else:
            i += 1
    missing = expected - given
    return int(missing.pop())

def main():
    import sys
    lines = sys.stdin.read().splitlines()
    M, N = map(int, lines[0].split())
    sequence_str = lines[1].strip()
    print(find_missing_number(M, N, sequence_str))


if __name__ == "__main__":
    main()