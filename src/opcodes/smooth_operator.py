def add(data, *args):
    in1, in2, out = args
    try:
        data[out] = in1 + in2
    except IndexError:
        print(out)
    return data


def multiply(data, *args):
    in1, in2, out = args
    data[out] = in1 * in2
    return data


def stop(data):
    return False


def save(data, in1):
    in2 = int(input(f"Enter value to save at {in1}"))
    data[in1] = in2
    return data


def read(data, *args):
    in1 = args
    print(data[in1])
    return data


operations = {
    1: (add, 3),
    2: (multiply, 3),
    3: (save, 1),
    4: (read, 1),
    99: (stop, 0)
}

def position(data, index):
    return data[index]

def immediate(data, number):
    return number

modes = {
    0: position,
    1: immediate
}

if __name__ == "__main__":
    for key, value in operations.items():
        print(f"Opcode: {key} Function Name: {value.__name__}")