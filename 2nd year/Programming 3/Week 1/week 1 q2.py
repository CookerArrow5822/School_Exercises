#!/usr/bin/env python3
question_string = "This is DCU!"

def move_vow(question_string):
    new_string = ""
    tracker_list = []
    vowels = "aeiouAEIOU"
    i = 0
    while i < len(question_string):
        if question_string[i] in vowels:
            new_string += question_string[i]

        else:
            tracker_list.append(question_string[i])

        i = i + 1

    for j in tracker_list:
        new_string += j

    return new_string



print (move_vow(question_string))




# put each letter into a list
# look for vowels in list
# add vowels to new string
# add each constanant back into the new string