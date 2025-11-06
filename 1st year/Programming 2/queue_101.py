#!/usr/bin/env python3

class Queue(object):

    def __init__(self):
        self.q = []

    def enqueue(self, e):
        self.q.append(e)
    
    def dequeue(self):
        return self.q.pop(0)

    def first(self):
        return self.q[0]

    def is_empty(self):
        return len(self.q) == 0
    
    def __len__(self):
        return len(self.q)