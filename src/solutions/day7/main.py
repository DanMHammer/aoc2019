import csv
from collections import deque
outputs = []
from itertools import permutations


def operate(data, pointer, inputs):
    commands = data[pointer]
    pointer += 1
    opcode = commands % 100
    parameters = [commands // 100 % 10, commands // 1000 % 10, commands // 10000 % 10]
    output = False

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
        in2 = inputs.popleft()
        pointer += 1
        data[in1] = in2
    elif opcode == 4:  # read
        in1 = data[pointer]
        pointer += 1
        output = data[in1]
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

    return data, pointer, inputs, output


def operation_loop(data, input1):
    inputs = deque([input1])
    output = 0
    pointer = 0
    while pointer >= 0:
        data, pointer, inputs, output = operate(data, pointer, inputs)
    return data, output


def amplifier(data, phases, i):
    if not phases:
        outputs.append(i)
        print("output", i)
    else:
        for phase in phases:
            output = operation_loop(data, phase, i)
            print(phase, output)
            amplifier(data, [x for x in phases if x != phase], output)


class Amp:
    def __init__(self, data, phase):
        self.data = data
        self.phase = phase
        self.out = 0
        self.con = True

    def run_operations(self, i=self.phase):
        print(self.data, self.phase, i)
        self.data, newout = operation_loop(self.data, i)
        if newout == false:
            self.con = False
        else:
            self.out = newout

    def get_output(self):
        return self.out, self.con

    def __str__(self):
        return str(self.phase)


class AmpGroup:
    def __init__(self, phases, data):
        self.amps = []
        self.data = data
        for phase in phases:
            self.amps.append(Amp(data[:], phase))
        self.out = 0

    def __str__(self):
        o = ""
        for idx, amp in enumerate(self.amps):
            o += f"Amp {idx}: {amp}\n"
        return o

    def run(self):
        while self.amps:
            for amp in self.amps:
                amp.run_operations(self.out)
                self.out, con = amp.get_output()
                if not con:
                    self.amps.remove(amp)
                print(self.out)
        return self.out


if __name__ == "__main__":
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        init_data = [int(x) for x in list(reader)[0]]
        # print(init_data)
        #
        # amplifier(init_data, [0, 1, 2, 3, 4], 0)
        #
        # print(outputs)
        # print(f"Answer One: {max(outputs)}")

        outputs = []

        for p in permutations(range(5, 10)):
            print(list(p))
            group = AmpGroup(list(p), init_data[:])
            print(group)
            outputs.append(group.run())

        print(f"Answer Two: {max(outputs)}")