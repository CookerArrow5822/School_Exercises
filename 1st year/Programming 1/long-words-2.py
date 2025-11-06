#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["dog", "cat", "mouse"]

s = ""
i = 0

while i < len(a) and len(s) < 6:
   s = a[i]
   i = i + 1

if i < len(a) or len(a) == 1:
   print(s)
