class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.heuristic = 0

    def add(self, dest, cost):
        edge = (dest, cost)
        self.edges.append(edge)