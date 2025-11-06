import sys

last_departure = 0  

for line in sys.stdin:
    arrival, name, duration = line.split()
    arrival, duration = int(arrival), int(duration)

    if arrival >= last_departure:
        last_departure = arrival + duration
    else:
        last_departure += duration

print(last_departure)
