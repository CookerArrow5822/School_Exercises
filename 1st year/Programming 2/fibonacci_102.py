#!/usr/bin/env python3

def fibonacci(N):
    if N == 0:
        return 1
    
    elif N == 1:
        return 1
    
    else:
        return fibonacci(N -1) + fibonacci(N - 2)