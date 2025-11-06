#!/usr/bin/env python3

if __name__ == "__main__":
   a = []
   s = ""

i = 0
while i < len(a):
   number = len(s)
   if a[i][:len(s)] == s:
      print(a[i])
   i = i + 1
