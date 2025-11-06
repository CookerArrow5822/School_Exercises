#!/usr/bin/env python3

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max(len(neighbors) for neighbors in self.adj)

    def avgDegree(self):
        return sum(len(neighbors) for neighbors in self.adj) / self.V

class BFSPaths:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * g.V
        self.edgeTo = [-1] * g.V
        self.bfs(s)

    def bfs(self, s):
        queue = []
        self.visited[s] = True
        queue.append(s)

        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.visited[w]:
                    self.edgeTo[w] = v
                    self.visited[w] = True
                    queue.append(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return []
        path = []
        while v != self.s:
            path.append(v)
            v = self.edgeTo[v]
        path.append(self.s)
        return path[::-1]
