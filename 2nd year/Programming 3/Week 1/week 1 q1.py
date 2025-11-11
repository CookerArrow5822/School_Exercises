#!/usr/bin/env python3

q1_sum = ([
    [1, 0, 2],
    [5, 5, 7],
    [9, 4, 3]
])

active_number = 0
total_even_sum = 0

i = 0
while i < len(q1_sum):
    active_list = q1_sum[i]
    i = i + 1

    j = 0
    while j < len(active_list):
        active_number = active_list[j]
        if active_number % 2 == 0:
            total_even_sum += active_number
        j = j + 1

print(total_even_sum)


# do it list by list using a nested for loop
# ensure a number is even
# add even numbers together
# print output