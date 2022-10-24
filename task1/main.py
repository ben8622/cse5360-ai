"""
Written by Benjamin Knight
1001788622

Assignment 1 for CSE 5360 - AI
"""


import sys
from classes.Node import Node
from classes.Statistics import Statistics
from classes.Algorithm import Algorithm

# algorithm args
cities: dict[str, Node] = {}
visited: dict[str, bool] = {}
fringe: list[Node] = []

if __name__ == "__main__":

    # pull command line arguments out
    file_path: str = sys.argv[1]
    starting_city: str = sys.argv[2]
    goal: str = sys.argv[3]

    # build cities
    with open(file_path) as f:
        for line in f.readlines():
            if line == "END OF INPUT": break

            start, end, cost = line.split()

            # convert cost to an int not string
            cost = int(cost)

            if start not in cities:
                cities[start] = Node(start)
            if end not in cities:
                cities[end] = Node(end)

            # create edges for each node on the edge
            cities[start].add(end, cost)
            cities[end].add(start, cost)

    # init fringe with starting city
    fringe.append(cities[starting_city])

    # initialize answer
    ans: Node = None
    statistics: Statistics = None

    # if heuristic provided, build it
    if(len(sys.argv) == 5):
        with open(sys.argv[4]) as f:
            for line in f.readlines():
                if(line == "END OF INPUT"): break

                city, heuristic = line.split()

                # convert heuristic to an int not string
                heuristic = int(heuristic)

                cities[city].heuristic = heuristic

    # perform the search
    algorithm: Algorithm = Algorithm()
    ans = algorithm.search(cities, fringe, visited, goal)

    algorithm.statistics.print_stats()

        


