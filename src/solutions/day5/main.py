import csv

def operate(data, pointer):
    commands = data[pointer]
    pointer += 1
    opcode = commands % 100
    parameters = [commands // 100 % 10, commands // 1000 % 10, commands // 10000 % 10]

    if opcode == 1:  # add
        if parameters[0] == 0:
            in1 = data[data[pointer]]
        else:
            in1 = data[pointer]
        if parameters[1] == 0:
            in2 = data[data[pointer + 1]]
        else:
            in2 = data[pointer + 1]
        out = data[pointer + 2]
        pointer += 3
        data[out] = in1 + in2
    elif opcode == 2:  # multiply
        if parameters[0] == 0:
            in1 = data[data[pointer]]
        else:
            in1 = data[pointer]
        if parameters[1] == 0:
            in2 = data[data[pointer + 1]]
        else:
            in2 = data[pointer + 1]
        out = data[pointer + 2]
        pointer += 3
        data[out] = in1 * in2
    elif opcode == 3:  # save
        in1 = data[pointer]
        in2 = int(input(f"Enter value to save at {in1}"))
        pointer += 1
        data[in1] = in2
    elif opcode == 4:  # read
        in1 = data[pointer]
        pointer += 1
        print(data[in1])
    elif opcode == 5: # jump-if-true:
        if parameters[0] == 0:
            in1 = data[data[pointer]]
        else:
            in1 = data[pointer]
        if parameters[1] == 0:
            in2 = data[data[pointer + 1]]
        else:
            in2 = data[pointer + 1]
        if in1 != 0:
            pointer = in2
        else:
            pointer += 2
    elif opcode == 6: # jump-if-false:
        if parameters[0] == 0:
            in1 = data[data[pointer]]
        else:
            in1 = data[pointer]
        if parameters[1] == 0:
            in2 = data[data[pointer + 1]]
        else:
            in2 = data[pointer + 1]
        if in1 == 0:
            pointer = in2
        else:
            pointer += 2
    elif opcode == 7:  # less-than
        if parameters[0] == 0:
            in1 = data[data[pointer]]
        else:
            in1 = data[pointer]
        if parameters[1] == 0:
            in2 = data[data[pointer + 1]]
        else:
            in2 = data[pointer + 1]
        out = data[pointer + 2]
        if in1 < in2:
            data[out] = 1
        else:
            data[out] = 0
        pointer += 3
    elif opcode == 8: # equal
        if parameters[0] == 0:
            in1 = data[data[pointer]]
        else:
            in1 = data[pointer]
        if parameters[1] == 0:
            in2 = data[data[pointer + 1]]
        else:
            in2 = data[pointer + 1]
        out = data[pointer + 2]
        if in1 == in2:
            data[out] = 1
        else:
            data[out] = 0
        pointer += 3
    elif opcode == 99:
        pointer = -1

    return data, pointer


def operation_loop(data):
    pointer = 0
    while pointer >= 0:
        data, pointer = operate(data, pointer)


if __name__ == "__main__":
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        init_data = list(reader)
        # print([int(x) for x in init_data[0]][1])
        operation_loop([int(x) for x in init_data[0]])