import sys
from Node import Node
from utilities import uninformed_search, informed_search

# algorithm args
cities: dict[str, Node] = {}
visited: dict[str, bool] = {}
fringe: list[Node] = []

if __name__ == "__main__":

    # pull command line arguments out
    file_path: str = sys.argv[1]
    starting_city: str = sys.argv[2]
    goal: str = sys.argv[3]

    # build graph
    with open(file_path) as f:
        for line in f.readlines():
            if(line == "END OF INPUT"): break

            start, end, cost = line.split()

            # convert cost to an int not string
            cost = int(cost)

            if(start not in cities):
                cities[start] = Node(start)
            if(end not in cities):
                cities[end] = Node(end)

            # create edges for each node on the edge
            cities[start].add(end, cost)
            cities[end].add(start, cost)

    # init fringe with starting city
    fringe.append(cities[starting_city])

    # initialize answer
    ans: Node = None

    # if heuristic provided, build it, perform informed search
    if(len(sys.argv) == 5):
        with open(sys.argv[4]) as f:
            for line in f.readlines():
                if(line == "END OF INPUT"): break

                city, heuristic = line.split()

                cities[city].heuristic = heuristic

        ans = informed_search(cities, fringe, visited, goal)
    
    # else, perform uninformed search
    else:
        ans = uninformed_search(cities, fringe, visited, goal)

    while(ans.prev != None):
        print(ans.name)
        ans = ans.prev

    print(ans.name)

        


