from assignment1.classes.Node import Node
import copy


def search(cities: dict[str, Node], fringe: list[Node], visited: dict[str, bool], goal: str):
    while (len(fringe) > 0):
        node = fringe.pop()

        # check if we have already proccessed this node (graph search)
        if (node.name in visited):
            continue

        # check if reached goal
        if (node.name == goal):
            return node

        # add node to visited
        visited[node.name] = True

        # expand node and add to the fringe
        fringe = expand_node(node, cities, fringe)

    # goal not found
    return None


def informed_search(cities: dict[str, Node], fringe: list[Node], visited: dict[str, bool], goal: str):
    exit()


def expand_node(node: Node, cities: dict[str, Node], fringe: list[Node]) -> list[Node]:
    for edge in node.edges:
        # pull out details of the edge
        end_city: str = edge[0]
        path_cost: int = edge[1]

        # grab end_city Node from cities
        end_city_node: Node = copy.deepcopy(cities[end_city])

        # fill in relevant information
        end_city_node.cost = path_cost + node.cost + end_city_node.heuristic
        end_city_node.prev = node

        # insert into fringe (in order)
        fringe = insert_node(end_city_node, fringe)

    return fringe


def insert_node(new: Node, fringe: list[Node]):
    for i in range(len(fringe)):
        node = fringe[i]

        # here we insert in order, for example new.cost = 4, fringe = [6, 4, 1, 1]
        # we will hit i = 1, and insert resulting fringe = [6, 4, 4, 1, 1]
        if node.cost <= new.cost:
            fringe.insert(i, new)
            return fringe

    # either fringe is empty or node has least cost and should be added to very end
    fringe.append(new)
    return fringe
