import pandas as pd


def traverse_path(path):
    positions = []
    x_movements = {"R": 1, "L": -1, "U": 0, "D": -0}
    y_movements = {"R": 0, "L": 0, "U": 1, "D": -1}
    step_dict = {}
    x, y = 0, 0

    steps = 0

    for instruction in path:
        direction = instruction[0]
        magnitude = int(instruction[1:])
        x_move = x_movements[direction]
        y_move = y_movements[direction]
        for num in range(0, magnitude):
            x += x_move
            y += y_move
            steps += 1
            positions.append((x, y))
            if ((x, y) in step_dict.keys() and step_dict[(x, y)] > steps) or ((x, y) not in step_dict.keys()):
                step_dict[(x, y)] = steps

    return positions, step_dict


if __name__ == "__main__":
    paths = pd.read_csv("./input.csv", header=None)
    wire1_path = paths.iloc[0].values
    wire2_path = paths.iloc[1].values

    wire1_positions, wire1_steps = traverse_path(wire1_path)
    wire2_positions, wire2_steps = traverse_path(wire2_path)

    da = {}
    distances = []
    least_steps = 1000000

    for x, y in wire1_positions:
        if x in da.keys():
            da[x].append(y)
        else:
            da[x] = [y]

    for x, y in wire2_positions:
        if x in da.keys() and y in da[x]:
            distances.append(abs(x) + abs(y))
            steps = wire1_steps[(x, y)] + wire2_steps[(x, y)]
            if steps < least_steps:
                least_steps = steps


    print(f"Part One: {min(distances)}")
    print(f"Part Two: {least_steps}")
