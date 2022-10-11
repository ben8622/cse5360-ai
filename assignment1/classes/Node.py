class Node:

    def __init__(self, name: str):
        self.name: str = name
        self.edges: list[tuple[str, int]] = []
        self.heuristic: int = 0
        self.prev: Node = None
        self.cost: int = 0

    def add(self, dest: str, cost: int):
        edge = (dest, cost)
        self.edges.append(edge)