class Statistics:
    def __init__(self):
        self.popped: int = 0
        self.expanded: int = 0
        self.generated: int = 1  # take account for initial node
        self.distance: int = 0
        self.route: list[str] = []

    def print_stats(self):
        print(f"Nodes Popped: {self.popped}")
        print(f"Nodes Expanded: {self.expanded}")
        print(f"Nodes Generated: {self.generated}")

        if self.distance > 0:
            print(f"Distance: {self.distance} km")
        else:
            print("Distance: infinity")

        print("Route:")
        if len(self.route) > 0:
            for s in self.route[::-1]:  # flips array
                print(s)
        else:
            print("None")
