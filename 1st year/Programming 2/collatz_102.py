#!/usr/bin/env python3

def collatz(N):
    print(N)
    if N == 1:
        return N
    
    elif N % 2 == 0:
        collatz(N // 2)
    
    else:
        collatz((N * 3) + 1)
    
