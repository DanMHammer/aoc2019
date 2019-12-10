import numpy as np


def are_not_collinear(a_x, a_y, b_x, b_y, c_x, c_y):
    return .5*np.linalg.det(np.array([[a_x-b_x, b_x-c_x], [a_y-b_y, b_y - c_y]])) != 0


if __name__ == "__main__":
    with open("input.txt") as file:
        field = []
        vision = []
        locations = []
        for line in file:
            field.append([char for char in line.rstrip()])

        field = np.array(field)

        for (x, y), value in np.ndenumerate(field):
            if value == "#":
                locations.append((x, y))

        for a_idx, (ax, ay) in enumerate(locations):
            vis = 0
            for b_idx, (bx, by) in enumerate(locations):
                if a_idx == b_idx:
                    pass
                else:
                    for c_idx, (cx, cy) in enumerate(locations):
                        if b_idx == c_idx:
                            pass
                        else:
                            if are_not_collinear(ax, ay, bx, by, cx, cy):
                                vis += 1
                                print("vision")
            vision.append(vis)

        print(max(vision))
