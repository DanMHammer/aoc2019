from src.opcodes.computer import Computer
import csv

if __name__ == "__main__":
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        init_data = [int(x) for x in list(reader)[0]]
        computer = Computer()
        computer.set_data(init_data)
        computer.start()