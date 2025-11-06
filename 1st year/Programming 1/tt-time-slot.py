#!/usr/bin/env python3

s = input()
end_hour = 0

while s != "end":
    toks = s.split()
    hour = int(toks[2])
    start_hour = toks[1]

    start_hour = int(start_hour) // 1
    if hour >= 2:
        end_hour = int(start_hour) + int(hour - 1)

    else:
        end_hour = start_hour

    a = toks[0]
    b = toks[3:]
    b = " ".join(b)

    sentence = a + " " + str(start_hour) + ":00" + " "
    sentence = sentence + str(end_hour) + ":50" + " " + b
    print(sentence)

    s = input()
