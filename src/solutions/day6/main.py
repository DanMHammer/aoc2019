class OrbitMap:
    def __init__(self):
        self.data = {}

    def add(self, orbit):
        o = orbit.split(")")
        center, orbiter = o[0], o[1]
        if center not in self.data.keys():
            self.data[center] = [orbiter]
        else:
            self.data[center].append(orbiter)
        if orbiter not in self.data.keys():
            self.data[orbiter] = []

    def count(self):
        indirect, direct = 0, 0
        for center, orbits in self.data.items():
            direct += len(orbits)
            for values in self.data.values():
                if center in values:
                    indirect += 1
        return indirect, direct

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        Orbits = OrbitMap()
        for line in file:
            Orbits.add(line.rstrip())
        indirect, direct = Orbits.count()
        print(indirect + direct)
        print(Orbits)