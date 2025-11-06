#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f"{self.hour:{0}>2}:{self.minute:{0}>2} ({self.duration} minutes)"

    def __lt__(self, other):
        return (self.hour, self.minute) < (other.hour, other.minute)

class Schedule(object):

    def __init__(self, schedule=None):
        self.schedule = []

    def add(self, meeting):
        self.schedule.append(meeting)
        self.schedule.sort()

    def __str__(self):
        result = "Schedule\n--------\n"
        for meeting in self.schedule:
            result += f"{str(meeting)}\n"
        result += f"Meetings today: {len(self.schedule)}"
        return result