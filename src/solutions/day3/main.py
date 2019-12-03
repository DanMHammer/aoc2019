import pandas as pd


def traverse_path(path):
    positions = []
    x_movements = {"R": 1, "L": -1, "U": 0, "D": -0}
    y_movements = {"R": 0, "L": 0, "U": 1, "D": -1}
    x, y = 0, 0

    for instruction in path:
        direction = instruction[0]
        magnitude = int(instruction[1:])
        x_move = x_movements[direction]
        y_move = y_movements[direction]
        for num in range(0, magnitude):
            x += x_move
            y += y_move
            positions.append((x, y))

    return positions


if __name__ == "__main__":
    paths = pd.read_csv("./input.csv", header=None)
    wire1_path = paths.iloc[0].values
    wire2_path = paths.iloc[1].values

    wire1_positions = traverse_path(wire1_path)
    wire2_positions = traverse_path(wire2_path)

    da = {}
    distances = []

    for x, y in wire1_positions:
        if x in da.keys():
            da[x].append(y)
        else:
            da[x] = [y]

    for x, y in wire2_positions:
        if x in da.keys() and y in da[x]:
            distances.append(abs(x) + abs(y))

    print(f"Part One: {min(distances)}")