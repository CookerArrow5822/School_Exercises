#!/usr/bin/env python3

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = {v: [] for v in range(V)}

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max(len(neighbors) for neighbors in self.adj.values())

    def avgDegree(self):
        return sum(len(neighbors) for neighbors in self.adj.values()) / self.V