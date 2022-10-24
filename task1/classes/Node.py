class Node:

    def __init__(self, name: str):
        self.name: str = name
        self.edges: list[tuple[str, int]] = []
        self.heuristic: int = 0
        self.prev: Node = None
        self.estimated_cost: int = 0
        self.true_cost: int = 0
        self.path_cost: int = 0  # cost to get to this node from prev

    def add(self, dest: str, cost: int):
        edge = (dest, cost)
        self.edges.append(edge)
