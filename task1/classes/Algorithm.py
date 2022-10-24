from .Node import Node
from .Statistics import Statistics
import copy


def insert_node(new: Node, fringe: list[Node]) -> list[Node]:
    for i in range(len(fringe)):
        node = fringe[i]

        # here we insert in order, for example new.cost = 4, fringe = [6, 4, 1, 1]
        # we will hit i = 1, and insert resulting fringe = [6, 4, 4, 1, 1]
        if node.estimated_cost <= new.estimated_cost:
            fringe.insert(i, new)
            return fringe

    # either fringe is empty or node has least cost and should be added to very end
    fringe.append(new)
    return fringe


class Algorithm:

    def __init__(self):
        self.statistics: Statistics = Statistics()

    def search(self, cities: dict[str, Node], fringe: list[Node], visited: dict[str, bool], goal: str) -> Node:
        while len(fringe) > 0:
            node = fringe.pop()
            self.statistics.popped += 1

            # check if we have already processed this node (graph search)
            if node.name in visited:
                continue

            # check if reached goal
            if node.name == goal:
                self.build_statistics(node)
                return node

            # add node to visited
            visited[node.name] = True

            # expand node and add to the fringe
            fringe = self.expand_node(node, cities, fringe)
            self.statistics.expanded += 1

        # goal not found
        return None

    def expand_node(self, node: Node, cities: dict[str, Node], fringe: list[Node]) -> list[Node]:
        for edge in node.edges:
            # pull out details of the edge
            end_city: str = edge[0]
            path_cost: int = edge[1]

            # grab end_city Node from cities
            end_city_node: Node = copy.deepcopy(cities[end_city])
            self.statistics.generated += 1

            # fill in relevant information
            end_city_node.estimated_cost = path_cost + node.estimated_cost + end_city_node.heuristic
            end_city_node.true_cost = path_cost + node.estimated_cost
            end_city_node.path_cost = path_cost
            end_city_node.prev = node

            # insert into fringe (in order)
            fringe = insert_node(end_city_node, fringe)

        return fringe

    def build_statistics(self, node: Node):
        while node.prev is not None:
            self.statistics.distance += node.path_cost
            s1 = f" to {node.name}, {node.path_cost} km"
            node = node.prev
            self.statistics.route.append(f"{node.name}" + s1)
