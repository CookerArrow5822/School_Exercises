#!/usr/bin/env python3

i = 0
if __name__ == "__main__":
   a = []

while i < len(a) and a[i] == "":
   i = i + 1

if i < len(a):
   print(a[i])
