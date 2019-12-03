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


def find_intersections(path1, path2):
    intersections = []
    for x in range(0, len(path1) - 1, 2):
        for y in range(0, len(path2) - 1, 2):
            res = intersect(path1[x:x+2], path2[y:y+2])
            if res:
                intersections.append(res)
            else:
                pass
    return intersections

def intersect(segment1, segment2):
    line1 = line(segment1[0], segment1[1])
    line2 = line(segment2[0], segment2[1])

    if not line1 or not line2:
        return False
    else:
        m1, x1 = line1
        m2, x2 = line2

        if m1 == m2:
            return False
        else:
            Ax, Ay = segment1[0]
            Bx, By = segment1[1]
            Cx, Cy = segment2[0]
            Dx, Dy = segment2[0]

            boundsX1 = (min(Ax, Bx), max(Ax, Bx))
            boundsY1 = (min(Ay, By), max(Ay, By))
            boundsX2 = (min(Cx, Dx), max(Cx, Dx))
            boundsY2 = (min(Cy, Dy), max(Cy, Dy))

            x = (b2 - b1)/(m1 - m2)
            y = m1 * x + b1

            if (boundsX1[0] <= x <= boundsX1[1] and
                boundsX2[0] <= x <= boundsX2[1] and
                boundsY1[0] <= y <= boundsY1[1] and
                boundsY2[0] <= y <= boundsY2[1]):
                return x, y
            else:
                return False


def line(point1, point2):
    print(f"Point 1 {point1}")
    print(f"Point 2 {point2}")
    x1, y1 = point1
    x2, y2 = point2

    if x2 - x1 == 0:
        return False
    else:
        slope = (y2 - y1)/(x2 - x1)
        intercept = y1 - slope * x1
        return slope, intercept


if __name__ == "__main__":
    paths = pd.read_csv("./input.csv", header=None)
    wire1_path = paths.iloc[0].values
    wire2_path = paths.iloc[1].values

    wire1_positions = traverse_path(wire1_path)
    wire2_positions = traverse_path(wire2_path)

    intersections = [find_intersections(wire1_positions, wire2_positions)]
    #distances = [abs(x) + abs(y) for x, y in intersections]


    # print(f"Part One: {min(distances)}")
    print(wire1_positions)
    print(wire2_positions)
    print(intersections)
    #print(distances)