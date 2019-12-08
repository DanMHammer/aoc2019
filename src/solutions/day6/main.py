class Body:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parent = None

    def add_child(self, child_name):
        self.children.add(child_name)

    def add_parent(self, parent):
        self.parent = parent

    def direct(self):
        return len(self.children)

    def indirect(self):
        if self.name == "COM":
            return 0
        node = self.parent
        distance = 0
        while node.name != "COM":
            distance += 1
            node = node.parent
        return distance



class OrbitMap:
    def __init__(self):
        self.bodies = dict()

    def load_body(self, parent, child):
        if parent not in self.bodies.keys():
            self.bodies[parent] = Body(parent)
        if child not in self.bodies.keys():
            self.bodies[child] = Body(child)
        self.bodies[parent].add_child(self.bodies[child])
        self.bodies[child].add_parent(self.bodies[parent])

    def direct(self):
        num = 0
        for body_name, body_object in self.bodies.items():
            num += body_object.direct()
        return num

    def indirect(self):
        num = 0
        for body_name, body_object in self.bodies.items():
            num += body_object.indirect()
        return num

    def you_to_santa(self):
        return self.bodies["YOU"].distance_to_santa()


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        Orbits = OrbitMap()
        for line in file:
            line = line.rstrip()
            parent, child = line.split(")")
            Orbits.load_body(parent, child)
        direct = Orbits.direct()
        indirect = Orbits.indirect()
        print(f"Direct: {direct}")
        print(f"Indirect: {indirect}")
        print(f"Part One: {direct + indirect}")
        print(f"Part Two: {Orbits.you_to_santa()}")

