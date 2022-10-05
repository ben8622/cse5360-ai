import sys
from Node import Node
from utilities import uninformed_search, informed_search

# command line args
filepath = ""
starting_city = ""
dest_city = ""
heuristic_path = ""

# algorithm args
cities = {}
heuristic = {}

if __name__ == "__main__":

    # pull command line arguments out
    file_path = sys.argv[1]
    starting_city = sys.argv[2]
    dest_city = sys.argv[3]

    # build graph
    with open(file_path) as f:
        for line in f.readlines():
            if(line == "END OF INPUT"): break

            start, end, cost = line.split()

            if(start not in cities):
                cities[start] = Node(start)
            if(end not in cities):
                cities[end] = Node(end)

            cities[start].add(end, cost)
            cities[end].add(start, cost)

    # if heuristic provided, build it, perform informed search
    if(len(sys.argv) == 5):
        with open(sys.argv[4]) as f:
            for line in f.readlines():
                if(line == "END OF INPUT"): break

                city, heuristic = line.split()

                cities[city].heuristic = heuristic

        informed_search(cities)
    
    # else, perform uninformed search
    else:
        uninformed_search(cities)

        


