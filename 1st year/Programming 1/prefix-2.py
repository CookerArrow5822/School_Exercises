#!/usr/bin/env python3

if __name__ == "__main__":
   a = []
   s = ""

i = 0
number = len(s)
while i < len(a) and a[i][:len(s)] == s:
   i = i + 1

if i < len(a):
   print(a[i])
