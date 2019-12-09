class Computer:
    def __init__(self):
        self.pointer = 0
        self.relative_base = 0
        self.data = []
        self.running = True
        self.codes = {
            1 : (self.add, 3),
            2: (self.multiply, 3),
            3: (self.input_data, 1),
            4: (self.output_data, 1),
            5: (self.jump_if_true, 2),
            6: (self.jump_if_false, 2),
            7: (self.less_than, 3),
            8: (self.equals, 3),
            9: (self.relative_base_offset, 1),
            99: (self.halt, 1)
        }
        self.cheater_memory = dict()

    def set_data(self, data):
        self.data = data

    def set_pointer(self, pointer):
        self.pointer = pointer

    def advance_pointer(self, count):
        self.pointer += count

    def update_reg(self, register, value):
        if register >= len(self.data):
            self.data[register] = value
        else:
            self.cheater_memory[register] = value

    def get_reg(self, register):
        if register >= len(self.data):
            if register in self.cheater_memory.keys():
                return self.cheater_memory[register]
            else:
                self.cheater_memory[register] = 0
                return 0
        else:
            return self.data[register]

    def cheat(self, register):
        if register in self.cheater_memory.keys():
            return self.cheater_memory[register]
        else:
            self.cheater_memory[register] = 0
            return 0

    def pm(self, param, in1):
        if param == 0:
            return self.get_reg(in1)
        elif param == 1:
            return in1
        elif param == 2:
            return self.get_reg(self.relative_base + in1)

    def operate(self):
        commands = self.data[self.pointer]
        opcode = commands % 100
        parameters = [commands // 100 % 10, commands // 1000 % 10, commands // 10000 % 10]
        function, num_args = self.codes[opcode]
        args = [self.pm(parameters[x], self.get_reg(self.pointer + x + 1)) for x in range(0, num_args)]
        print(commands, opcode, parameters, function.__name__, args)
        return function(*tuple(args))

    def start(self):
        while self.running:
            self.operate()

    def add(self, in1, in2, out):  # 1
        self.update_reg(out, in1 + in2)
        self.advance_pointer(4)

    def multiply(self, in1, in2, out):  # 2
        self.update_reg(out, in1 * in2)
        self.advance_pointer(4)

    def input_data(self, out):  # 3
        in1 = input("Input Value")
        self.update_reg(out, in1)
        self.advance_pointer(2)

    def output_data(self, in1):  # 4
        print(self.get_reg(in1))
        self.advance_pointer(2)

    def jump_if_true(self, in1, in2):   #5
        if in1 != 0:
            self.set_pointer(in2)
        else:
            self.advance_pointer(3)

    def jump_if_false(self, in1, in2):   #6
        if in1 == 0:
            self.set_pointer(in2)
        else:
            self.advance_pointer(3)

    def less_than(self, in1, in2, out):   #7
        if in1 < in2:
            self.update_reg(out, 1)
        else:
            self.update_reg(out, 0)
        self.advance_pointer(4)

    def equals(self, in1, in2, out):   #8
        if in1 == in2:
            self.update_reg(out, 1)
        else:
            self.update_reg(out, 0)
        self.advance_pointer(4)

    def relative_base_offset(self, in1):  #9
        self.relative_base = self.relative_base + in1
        self.advance_pointer(2)

    def halt(self, *args):  # 99
        self.running = False
