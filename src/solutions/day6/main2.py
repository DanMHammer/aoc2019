class OrbitMap:
    def __init__(self):
        self.direct = {}
        self.indirect = {}

    def add(self, orbit):
        o = orbit.split(")")
        center, orbiter = o[0], o[1]
        if center not in self.direct.keys():
            self.direct[center] = [orbiter]
        else:
            self.direct[center].append(orbiter)
        if orbiter not in self.indirect.keys():
            self.indirect[orbiter] = [center]
        else:
            self.indirect[orbiter].append(center)

    def count(self):
        direct, indirect = 0, 0
        for center, orbits in self.direct.items():
            direct += len(orbits)
        for orbiter, centers in self.indirect.items():
            indirect += len(centers)
            for x in centers:
                indirect += len(self.direct[x])

        return direct, indirect

    def __str__(self):
        return f"Direct: {self.direct}\n\nIndirect: {self.indirect}"


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        Orbits = OrbitMap()
        for line in file:
            Orbits.add(line.rstrip())
        direct, indirect = Orbits.count()
        print(direct + indirect)
        print(Orbits)