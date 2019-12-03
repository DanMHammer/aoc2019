import pandas as pd


def traverse_path(path):
    x, y = 0, 0
    # Exclude starting position
    positions = []
    for instruction in path:
        if instruction[0] == "R":
            x += int(instruction[1:])
        elif instruction[0] == "L":
            x -= int(instruction[1:])
        if instruction[0] == "U":
            y += int(instruction[1:])
        if instruction[0] == "D":
            y -= int(instruction[1:])
        positions.append((x, y))
    return positions

if __name__ == "__main__":
    paths = pd.read_csv("./input.csv", header=None)
    wire1_path = paths.iloc[0].values
    wire2_path = paths.iloc[1].values

    wire1_positions = set(traverse_path(wire1_path))
    wire2_positions = set(traverse_path(wire2_path))

    intersections = wire1_positions.intersection(wire2_positions)

    distances = []

    for i in intersections:
        a, b = i
        distances.append(abs(a) + abs(b))

    # print(f"Part One: {min(distances)}")
    print(wire1_positions)