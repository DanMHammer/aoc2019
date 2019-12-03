def fuel_eq(n):
    return n / 3 // 1 - 2


if __name__ == "__main__":
    with open("../inputs/day1.txt", "r") as file:
        fuel = 0
        for line in file:
            newFuel = fuel_eq(int(line))
            while newFuel > 0:
                fuel += newFuel
                newFuel = fuel_eq(newFuel)
        print(fuel)